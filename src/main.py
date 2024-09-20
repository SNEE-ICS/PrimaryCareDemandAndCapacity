import simpy
import numpy as np
import pandas as pd
import datetime as dt
from collections import defaultdict
from typing import Union

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
class StaffMember:
    def __init__(self, env, staff_type, fte):
        self.env = env  # SimPy environment
        self.staff_type = staff_type  # Type of staff (e.g., GP)
        self.daily_time = fte*450  # Available time per day in minutes
        self.staff_resource = simpy.Resource(env, capacity=1)  # SimPy resource with capacity of 1
        self.available_time = 450  # Initially, all daily time is available

    def use_time(self, duration):
        self.available_time -= duration  # Deduct the appointment duration from available time
        if self.available_time < 0:
            self.available_time = 0  # Ensure available time does not go below zero

class DailyModel:
    def __init__(self, date, run_number, region, demand_scenario, capacity_policy):

        env = simpy.Environment()
        n_patients = get_patient_demand(date, region, demand_scenario)
        availiable_staff = get_staff_by_date(date, region, capacity_policy)
        general_practitioners = [StaffMember(env, "GP", 1) for _ in range(availiable_staff["GP"])]
        other_practice_staff = [StaffMember(env, "Other practice staff", 1) for _ in range(availiable_staff["Other practice staff"])]
        unknown_staff = [StaffMember(env, "Unknown", 1) for _ in range(availiable_staff["Unknown"])]
        for patient in range(n_patients):
            # replace with proper distribution/choice by region
            staff_choice = np.random.choice([general_practitioners, other_practice_staff, unknown_staff])
            # treatment mode 
            appointment_mode = np.random.choice(["face-to-face", "telephone", "video"])
            appointment_duration = get_appointment_duration(region, appointment_mode)
            # no show
            no_show = get_no_show_prob(region)
            # patient process
            env.process(patient_process(env, staff_choice, appointment_duration, no_show))
        
        env.run()
        




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
