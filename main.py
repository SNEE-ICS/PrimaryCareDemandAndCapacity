import simpy
import numpy as np
import pandas as pd
import datetime as dt
from collections import defaultdict
from typing import Dict, Literal, Optional, Union
from tqdm import tqdm
from icecream import ic

from src.simulation_schemas import AreaAppointmentTimeDistributions, DeliveryPropensityByArea, PopulationScenarios, DidNotAttendRatesByArea, ClinicalStaffFTEByArea, MonthlyAppointmentForecast, StaffPropensityByArea
from src.various_methods import is_working_day


# Class representing an individual staff member
class StaffMembers:
    def __init__(self, staff_type:Literal['GP','Other practice staff','Unknown'], fte:float):
        self.staff_type = staff_type  # Type of staff (e.g., GP)
        self.initial_time = fte*450  # Available time per day in minutes
        self.available_time = 450  # Initially, all daily time is available

    def use_time(self, duration):
        self.available_time -= duration  # Deduct the appointment duration from available time
        if self.available_time < 0:
            self.available_time = 0  # Ensure available time does not go below zero

class SimulationData:


    def __init__(self):

       
        #population scenarios
        self.population_scenarios:PopulationScenarios = PopulationScenarios.read_yaml("outputs/population_projections.yaml")
        # staffing levels
        self.staff_fte = ClinicalStaffFTEByArea.read_yaml("outputs/staff_fte.yaml")
        # did not attend
        self.did_not_attend_rates = DidNotAttendRatesByArea.read_yaml("outputs/assumptions/dna_appointments.yaml")
        self.appointment_forecasts = MonthlyAppointmentForecast.read_yaml("outputs/ets_forecast_results.yaml")
        self.staff_type_propensity = StaffPropensityByArea.read_yaml("outputs/assumptions/staff_propensity.yaml")
        self.appointment_mode_propensity = DeliveryPropensityByArea.read_yaml("outputs/assumptions/appointment_modes.yaml")
        self.appointment_durations = AreaAppointmentTimeDistributions.read_yaml("outputs/assumptions/appointment_duration.yaml")
 
        

class DailyRegionalModel:
    def __init__(self, sim_data:SimulationData, date:dt.date, run_number:int, region:str, demand_scenario:str, capacity_policy:str, n_appointments:Optional[int]=None):
        
        self.sim_data = sim_data
        self.date = date
        self.run_number = run_number
        self.region = region
        self.demand_scenario = demand_scenario
        self.capacity_policy = capacity_policy

        if n_appointments is None:
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

        self.staff = {staff_type:StaffMembers(staff_type, fte) for staff_type, fte in self.availiable_staff.items()}
        
        self.fufilled_appointments = {staff_type:0 for staff_type in staff_types}
        self.no_show_appointments = {staff_type:0 for staff_type in staff_types}
        self.unmet_demand_appointments = {staff_type:0 for staff_type in staff_types}

        self.fufilled_minutes = {staff_type:0 for staff_type in staff_types}
        self.unmet_demand_minutes = {staff_type:0 for staff_type in staff_types}
        self.no_show_minutes = {staff_type:0 for staff_type in staff_types}
        
    
    def process_day(self):
        for patient in range(self.n_patients):
            # Choose a staff type
            staff_type:str = self.sim_data.staff_type_propensity.pick_staff_type(self.region)
            # Choose an appointment mode
            appointment_mode:str = self.sim_data.appointment_mode_propensity.get_appointment_mode(area=self.region,staff_type=staff_type)
            # Choose an appointment duration
            duration:int = self.sim_data.appointment_durations.get_area(self.region).get_time()
            # Check if the staff member is available
            if self.staff[staff_type].available_time != 0:
                self.staff[staff_type].use_time(duration)
                # determine if they show up
                # they can only no show if they actually get an appointment
                # returns True if they attended
                if not self.sim_data.did_not_attend_rates.did_patient_attend(area=self.region, staff_type=staff_type, appointment_mode=appointment_mode):
                    self.no_show_appointments[staff_type] += 1
                    self.no_show_minutes[staff_type] += duration
                else:
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
                                daily_model = DailyRegionalModel(sim_data=simulation_data, date=day, run_number=simulation_run, region=region, demand_scenario=population_scenario, capacity_policy=capacity_policy, n_appointments=num_appointments)
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