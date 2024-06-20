import simpy
import numpy as np
import pandas as pd
import datetime as dt
from collections import defaultdict
from typing import Dict, Literal, Union

STAFF_TYPES = ["GP", "Other practice staff", "Unknown"]
def get_staff_type(region):
    yield np.random.choice(STAFF_TYPES)


STAFF_LEVELS = {"GP": 50, "Other practice staff": 50, "Unknown": 30}
def get_n_staff(date:Union[str,dt.datetime],staff_type:str, region:str):
    pass

NO_SHOW_PROBS = {"06L": 0.1,
               "07K": 0.01,
               "06T": 0.011}
def get_no_show_prob(region):
    # based on the probability, yield true or false
    prob = NO_SHOW_PROBS[region]
    yield np.random.rand() > prob


def get_appointment_duration(region, appointment_mode):
    # sample from a distribution
    yield np.random.exponential(20)

# Class representing an individual staff member
class StaffMembers:
    def __init__(self, env, staff_type:Literal['GP','Other practice staff','unknown'], fte:float):
        self.env = env  # Access to the simulation environment
        self.staff_type = staff_type  # Type of staff (e.g., GP)
        self.inital_time = fte*450  # Available time per day in minutes
        self.available_time = 450  # Initially, all daily time is available

    def use_time(self, duration):
        self.available_time -= duration  # Deduct the appointment duration from available time
        if self.available_time < 0:
            self.available_time = 0  # Ensure available time does not go below zero

class DailyModel:
    def __init__(self, env, date:dt.date, run_number:int, region:str, demand_scenario:str, capacity_policy:str):

        self.env = env
        self.date = date
        self.run_number = run_number
        self.region = region
        self.demand_scenario = demand_scenario
        self.capacity_policy = capacity_policy

        self.n_patients = get_patient_demand(date, region, demand_scenario, forecast_method)
        self.availiable_staff:Dict[str,float] = get_staff_by_date(date, region, capacity_policy)
        self.staff = {staff_type:StaffMembers(env, staff_type, fte) for staff_type, fte in self.availiable_staff.items()}
        
        self.fufilled_appointments = {staff_type:0 for staff_type in STAFF_TYPES}
        self.no_show_appointments = {staff_type:0 for staff_type in STAFF_TYPES}
        self.unmet_demand_appointments = {staff_type:0 for staff_type in STAFF_TYPES}

        self.fufilled_minutes = {staff_type:0 for staff_type in STAFF_TYPES}
        self.unmet_demand_minutes = {staff_type:0 for staff_type in STAFF_TYPES}
        self.no_show_minutes = {staff_type:0 for staff_type in STAFF_TYPES}
        
    
        def process_day(self):
            for patient in range(self.n_patients):
                # Get the appointment duration
                duration:int = get_appointment_duration(region, appointment_mode)
                # Use the appointment duration
                staff_type:str = get_staff_type(region)
                if self.staff[staff_type].available_time != 0:
                    self.staff[staff_type].use_time(duration)
                    # determine if they show up
                    if check_no_show(region, staff_type):
                        self.no_show_appointments[staff_type] += 1
                        self.no_show_minutes[staff_type] += duration
                    else:
                        self.fufilled_appointments[staff_type] += 1
                        self.fufilled_minutes[staff_type] += duration 
                else:
                    self.unmet_demand_appointments[staff_type] += 1
                    self.unmet_demand_minutes[staff_type] += duration
                    

                # Yield the simulation environment to the next event
                return
        




def run_simulation(demand_scenarios, capacity_policies):
    env = simpy.Environment()
    runs = 1000
    run_outputs = []
    for simulation_run in range(runs):
        for demand_scenario in ['demand_scenario']:
            # load demand data
            # optionally do we want to do confidence intervals?
            for capacity_scenario in ['intervention_policy']:
                # load intervention policy
                for region in demand_data.keys():
                    region_demand = demand_data[region]
                    region_staff = staff_data[region]
                    staff = simpy.Resource(env, capacity=len(staff_types))
                    env.process(patient_process(env, region, staff, demand_per_staff, acute_referrals, unmet_demand))
            
    env.run()

    return demand_per_staff, acute_referrals, unmet_demand



if __name__ == '__main__':
        
    demand_per_staff, acute_referrals, unmet_demand = run_simulation()

    pd.Series(acute_referrals).to_csv('acute_referrals.csv', header=['Acute referrals'])

    pd.Series(unmet_demand).to_csv('unmet_demand.csv', header=['Unmet demand'])
