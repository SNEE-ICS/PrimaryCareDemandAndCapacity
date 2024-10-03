import numpy as np
import pandas as pd
import datetime as dt
import random
from collections import defaultdict
from typing import Dict, Literal, Optional, Union, Tuple
from tqdm import tqdm
from icecream import ic

from src.simulation_schemas import (AreaAppointmentTimeDistributions, 
                                    DeliveryPropensityByArea, 
                                    PopulationScenarios, 
                                    DidNotAttendRatesByArea, 
                                    ClinicalStaffFTEByArea, 
                                    MonthlyAppointmentForecast, 
                                    StaffPropensityByArea)
from src.various_methods import is_working_day
from src.constants import (SARIMA_FORECAST_OUTPUT_FILENAME, 
                           APPOINTMENT_DURATION_OUTPUT_FILENAME, 
                           STAFF_TYPE_PROPENSITY_OUTPUT_FILENAME, 
                           APPOINTMENT_MODE_PROPENSITY_OUTPUT_FILENAME, 
                           POPULATION_PROJECTIONS_OUTPUT_FILENAME,
                           ACUTE_REFERRAL_RATES_OUTPUT_FILENAME)

MINUTES_PER_DAY:int = 450
CONSTRAINED_APPOINTMENT_RANGE:Tuple[int] = (25,28)


# Class representing an individual staff member
class StaffMembers:
    def __init__(self,
                 staff_type:Literal['GP','Other practice staff','Unknown'], 
                 fte:float, 
                 appointment_limit:bool=False):
        """
        Initializes a staff member object, this is effectively a pool of staff resources for 1 working day.

        Parameters:
        - staff_type: The type of staff member (e.g., 'GP', 'Other practice staff', 'Unknown').
        - fte: The full-time equivalent (FTE) value of the staff member.
        - appointment_limit: Whether the staff member practices safe appointment scheduling. Defaults to False.

        Attributes:
        - staff_type: The type of staff member.
        - initial_time: The available time per day in minutes, calculated based on the FTE value.
        - available_time: The initially available time per day in minutes.
        - safe_practice: Whether the staff member practices safe appointment scheduling.
        - initial_appointments: The initial number of appointments per day, calculated based on the FTE value and safe_practice.
        - available_appointments: The initially available number of appointments per day.

        """
        self.staff_type = staff_type  # Type of staff (e.g., GP)
        self.initial_time = fte* MINUTES_PER_DAY  # Available time per day in minutes
        self.available_time = self.initial_time  # Initially, all daily time is available
        self.safe_practice = appointment_limit  # Whether the staff member practices safe appointment scheduling
        if appointment_limit: # give them a set number of appointments per day.
            appts = 0 
            for i in range(int(fte)):
                # make a set of appointments for each FTE
                appts += random.randint(*CONSTRAINED_APPOINTMENT_RANGE) # 25-28 appointments per day per fte if constrained 
                # find the remainder and multiply by the random number of appointments
                remainder = int((fte - int(fte)) * random.randint(*CONSTRAINED_APPOINTMENT_RANGE))
            self.initial_appointments = appts + remainder
            self.available_appointments = self.initial_appointments
        else:
            # these aren't constrained
            self.initial_appointments = fte * 99
            self.available_appointments = fte * 99

    def patient_request_appointment(self, appointment_duration:float)->bool:
        """
        Checks if a patient can request an appointment based on the availability of appointments and time.

        Args:
            appointment_duration (float): The duration of the appointment in minutes.

        Returns:
            bool: True if the patient request is successful
        """
        # if safe_practice, then constrain appointments & appointment time
        if self.safe_practice:
            if self.available_appointments > 0 and self.available_time >= appointment_duration:
                self.available_appointments -= 1
                self.available_time -= appointment_duration
                return True
            else:
                return False
        else:
            # only depends on time, safe practice is not observed
            if self.available_time >= appointment_duration:
                self.available_time -= appointment_duration
                return True
            else:
                return False


class SimulationData:
    """
    This class effectively holds all the data calculated from the notebooks in one big class.
    Might be approprate to break this into several classes in time.
    """


    def __init__(self):

       
        #population scenarios
        self.population_scenarios:PopulationScenarios = PopulationScenarios.read_yaml(POPULATION_PROJECTIONS_OUTPUT_FILENAME)
        # staffing levels
        self.staff_fte = ClinicalStaffFTEByArea.read_yaml("outputs/staff_fte.yaml")
        # prpoensity to attend
        self.did_not_attend_rates = DidNotAttendRatesByArea.read_yaml("outputs/assumptions/dna_appointments.yaml")
        # DEMAND SCENARIOS
        self.appointment_forecasts = {'SARIMA' : SARIMA_FORECAST_OUTPUT_FILENAME,
                                      'Regression - Principle Projection': None,
                                      'Regression - High International Migration Variant':None,
                                      'Regression - Low International Migration Variant': None
        } # TODO: Complete these
        self.staff_type_propensity = StaffPropensityByArea.read_yaml(STAFF_TYPE_PROPENSITY_OUTPUT_FILENAME)
        self.appointment_mode_propensity = DeliveryPropensityByArea.read_yaml(APPOINTMENT_MODE_PROPENSITY_OUTPUT_FILENAME)
        self.appointment_durations = AreaAppointmentTimeDistributions.read_yaml(APPOINTMENT_DURATION_OUTPUT_FILENAME)
        self.referral_rates = ACUTE_REFERRAL_RATES_OUTPUT_FILENAME # TODO: make schema
    
        

class DailyRegionalModel:
    def __init__(self, sim_data:SimulationData, date:dt.date, run_number:int, region:str, demand_scenario:str, capacity_policy:str, n_appointments:Optional[int]=None):
        
        self.sim_data = sim_data
        self.date = date
        self.run_number = run_number
        self.region = region
        self.demand_scenario = demand_scenario
        self.capacity_policy = capacity_policy

        if n_appointments is None:
            # this is where we get the forecast data
            self.n_patients = 5000 # TODO: get_forecast data by date
            # self.n_patients = sim_data.appointment_forecasts.get_forecast(date, region, demand_scenario)
        else:
            self.n_patients = n_appointments


        loaded_staff_data = sim_data.staff_fte.get_area(region).model_dump()

        #TODO: this is wrong, the staff types are difficult to infer from the previous excel model.
        staff_type_map = {"gp":"GP","nurses":"Other Practice Staff","direct_patient_care": "Unknown"}
        staff_types = staff_type_map.values()
        #rename keys to GP, Other practice staff, Unknown
        self.availiable_staff:Dict[str,float] = {staff_type_map[k]:v for k,v in loaded_staff_data.items()}

        # staff parameters, this holds a dictionary of staff types, and the 
        self.staff = {staff_type:StaffMembers(staff_type, fte) for staff_type, fte in self.availiable_staff.items()}
        
        # appointments output
        self.fufilled_appointments = {staff_type:0 for staff_type in staff_types}
        self.no_show_appointments = {staff_type:0 for staff_type in staff_types}
        self.unmet_demand_appointments = {staff_type:0 for staff_type in staff_types}

        # minutes output
        self.fufilled_minutes = {staff_type:0 for staff_type in staff_types}
        self.unmet_demand_minutes = {staff_type:0 for staff_type in staff_types}
        self.no_show_minutes = {staff_type:0 for staff_type in staff_types}
        
    
    def process_day(self):
        """
        - Each patient is processed in turn. 
        - The patient is assigned to a staff member based on the population propensity to see each staff member.
        The patient is then assigned an appointment mode based on the staff member's propensity to use that mode. 
        The patient is then assigned an appointment duration based on the staff member's propensity to use that duration. 
        The patient is then assigned an appointment time based on the staff member's availability. 
        If the staff member is available, the patient is assigned to that staff member. If the staff member is not available, the patient is assigned to the unmet demand.
        """
        for patient in range(self.n_patients):
            # Choose a staff type
            staff_type:str = self.sim_data.staff_type_propensity.pick_staff_type(self.region)
            # Choose an appointment mode
            appointment_mode:str = self.sim_data.appointment_mode_propensity.get_appointment_mode(area=self.region,staff_type=staff_type)
            # Choose an appointment duration
            duration:int = self.sim_data.appointment_durations.get_area(self.region).get_time()
            # Check if the staff member is available
            if self.staff[staff_type].patient_request_appointment(duration):
                # determine if they show up
                # they can only no show if they actually get an appointment!!
                # returns True if they attended
                if not self.sim_data.did_not_attend_rates.did_patient_attend(area=self.region, staff_type=staff_type, appointment_mode=appointment_mode):
                    # patient did not attend
                    self.no_show_appointments[staff_type] += 1
                    self.no_show_minutes[staff_type] += duration
                else:
                    # patient attended
                    self.fufilled_appointments[staff_type] += 1
                    self.fufilled_minutes[staff_type] += duration 
            else:
                self.unmet_demand_appointments[staff_type] += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                self.unmet_demand_minutes[staff_type] += duration                                                                
                
            return
        
    @property
    def summary(self):
        return {
            'fufilled_appointments':self.fufilled_appointments,
            'no_show_appointments':self.no_show_appointments,
            'unmet_demand_appointments':self.unmet_demand_appointments,
            'fufilled_minutes':self.fufilled_minutes,
            'no_show_minutes':self.no_show_minutes,
            'unmet_demand_minutes':self.unmet_demand_minutes
        }
        


def run_simulation(start_date:dt.date,end_date:dt.date, n_runs:int):

    ic("Starting Simulation")
    simulation_data = SimulationData()

    run_outputs = {}
    # iterate through the runs
    print("\n*****\n")
    for simulation_run in tqdm(range(n_runs)):
        # set empty outputs
        ic(simulation_run)
        run_outputs[simulation_run] = {}
        # iterate through the population scenarios
        for population_scenario in ['Principal Projection']: # TODO: add in other population scenarios
            # set empty outputs
            ic(population_scenario)
            run_outputs[simulation_run][population_scenario] = {}
            # iterate through the forecast methods
            for forecast_method in ['baseline_statistical_forecast']: # TODO: add in other forecast methods
                run_outputs[simulation_run][population_scenario][forecast_method] = {}
      
                # iterate through the capacity policies
                for capacity_policy in ['Do Nothing']:

                    run_outputs[simulation_run][population_scenario][forecast_method][capacity_policy] = {}
                    # iterate through the regions
                    for region in tqdm(['06L','07K','06T']):
                        run_outputs[simulation_run][population_scenario][forecast_method][capacity_policy][region] = {}
                        # iterate through the dates
                        for day in tqdm(pd.date_range(start=start_date,end=end_date)):
                            if is_working_day(day):

                                num_appointments =simulation_data.appointment_forecasts.get_forecast(region,day)
                                
                                run_outputs[simulation_run][population_scenario][forecast_method][capacity_policy][region][day] = {}
                                # run the simulation
                                daily_model = DailyRegionalModel(
                                    sim_data=simulation_data, 
                                    date=day, 
                                    run_number=simulation_run, 
                                    region=region, 
                                    demand_scenario=population_scenario, 
                                    capacity_policy=capacity_policy, 
                                    n_appointments=num_appointments)
                                daily_model.process_day()
                                # save the outputs
                            else:
                      
                                pass # non-working day




    return run_outputs

# Number of runs for the simulation


if __name__ == '__main__':
        
    simulation_outputs = run_simulation(
        start_date = dt.date(2024,6,1),
        end_date = dt.date(2034,5,31)
        ,n_runs=10)
    

    pd.DataFrame(simulation_outputs).to_csv("outputs/simulation_outputs.csv")