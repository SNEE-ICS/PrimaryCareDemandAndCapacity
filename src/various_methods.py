import calendar
import numpy as np
import datetime as dt
import pandas as pd
from dataclasses import dataclass
import math
from functools import lru_cache

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
        """Generates a unique plot name based on the current count"""
        current_count = self.count
        self.count += 1 # increment count
        return f"{const.NOTEBOOK_OUTPUT_FIGURES_PATH}{self.name}_{current_count}"
    

@lru_cache(maxsize=12)
def _month_to_angle(month:int)->float:
    """
    Converts a month (1-12) to its corresponding angle in radians.

    Parameters:
    month (int): The month to convert.

    Returns:
    float: The angle in radians.

    Raises:
    ValueError: If the month is not in the range 1-12.
    """
    if month not in range(1,13):
        raise ValueError('month must be in range 1-12')
    return month*2*math.pi/12

@lru_cache(maxsize=12)
def month_num_to_sin(month:int)->float:
    """
    Converts a month number to its corresponding sine value.

    Args:
        month (int): The month number (1-12).

    Returns:
        float: The sine value of the month number.

    Raises:
        ValueError: If the month number is not in the range 1-12.
    """
    if month not in range(1,13):
        raise ValueError('month must be in range 1-12')
    return math.sin(_month_to_angle(month))

@lru_cache(maxsize=12)
def month_num_to_cos(month:int)->float:
    """
    Convert the month number to its corresponding cosine value.

    Parameters:
    month (int): The month number (1-12).

    Returns:
    float: The cosine value of the month number.
    """
    if month not in range(1,13):
        raise ValueError('month must be in range 1-12')
    return math.cos(_month_to_angle(month))
