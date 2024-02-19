import calendar
import numpy as np
import datetime as dt
import pandas as pd
from dataclasses import dataclass
import math
from functools import lru_cache

from src.schemas import DataCatalog
import src.constants as const


def get_numdays(df_:pd.DataFrame):
    month_values = df_.index.get_level_values('APPOINTMENT_MONTH')
    years, months =  month_values.year, month_values.month

    def _num_days_in_month(year:int, month:int):
        # to be used by np.vectorize
        return calendar.monthrange(year, month)[1]

    num_days_in_month_v_ = np.vectorize(_num_days_in_month)

    return num_days_in_month_v_(years,months)

def get_workingdays(a_:np.array):
    years, months =  a_.year, a_.month

    #
    def _num_workingdays_in_month(year,month):
        workingdays = 0
        day = 1
        while day <= calendar.monthrange(year,month)[1]:
            the_date =  dt.datetime(year,month,day)
            if the_date.isoweekday() < 6 and the_date not in const.ENGLAND_BANK_HOLIDAYS:
                workingdays +=1
            day += 1
        return workingdays

    vec_workingdays = np.vectorize(_num_workingdays_in_month)
    return vec_workingdays(years, months)


def calc_oadr_status(ons_age_group:str):

    ons_age_group = ons_age_group.replace(" and over", "")
    try:
        ons_age = int(ons_age_group)
    except ValueError:
        return None
    if ons_age < 65 and ons_age >=20:
        return 'Working'
    elif ons_age >=65:
        return 'Retired'
    else:
        return None
    

@dataclass
class PlotCounter:
    """simple object to count plots in each notebook run
    and conveniently make names"""
    name: str
    count: int = 1

    @property
    def plot_name(self):
        # temporary variable to hold count whilst incremented
        current_count = self.count
        self.count += 1 # increment count
        return f"{const.NOTEBOOK_OUTPUT_FIGURES_PATH}{self.name}_{current_count}"
    

@lru_cache(maxsize=12)
def _month_to_angle(month:int)->float:
    if month not in range(1,13):
        raise ValueError('month must be in range 1-12')
    return month*2*math.pi/12

@lru_cache(maxsize=12)
def month_num_to_sin(month:int)->float:
    if month not in range(1,13):
        raise ValueError('month must be in range 1-12')
    return math.sin(_month_to_angle(month))

@lru_cache(maxsize=12)
def month_num_to_cos(month:int)->float:
    if month not in range(1,13):
        raise ValueError('month must be in range 1-12')
    return math.cos(_month_to_angle(month))


def get_staff_type():
    
    # Loading the GP workforce or staffing level dataset
    data_catalog = DataCatalog.load_from_yaml("data_catalog.yaml")
    workforce_data_catalog_entry_22 = data_catalog.single_data_sources[4]
    gp_workforce_df = workforce_data_catalog_entry_22.load()
    
    # Initialising a dictionary object to store staff type
    staff_type = {}
    apprentices_type = {}
    
    # Iterating over each rows of GP workforce dataframe
    for index, row in gp_workforce_df.iterrows():
        key = row["STAFF_ROLE"]
        value = row["STAFF_GROUP"]
        
        if key != 'Apprentices':
            if key in staff_type:
                if value not in staff_type[key]:
                    staff_type[key].append(value)
                # If the key already exist and has a list with single value, replace the list with single value directly
                elif len(staff_type[key]) == 1:
                    staff_type[key] = value
            else:
                staff_type[key] = [value]
               
        # Separate Dictionary for apprentices        
        else:
            if key in apprentices_type:
                if value not in apprentices_type[key]:
                    apprentices_type[key].append(value) 
            else:
                apprentices_type[key] = [value]
            
            
    # Sorting the dictionary on keys
    staff_type_sorted = dict(sorted(staff_type.items()))
                
    return staff_type_sorted, apprentices_type