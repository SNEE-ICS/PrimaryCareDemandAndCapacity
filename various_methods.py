import calendar
import numpy as np
import datetime as dt

import constants as const
import pandas as pd

def get_numdays(df_:pd.DataFrame):
    month_values = df_.index.get_level_values('APPOINTMENT_MONTH')
    years, months =  month_values.year, month_values.month

    def _num_days_in_month(year:int, month:int):
        # to be used by np.vectorize
        return calendar.monthrange(year, month)[1]

    num_days_in_month_v_ = np.vectorize(_num_days_in_month)

    return num_days_in_month_v_(years,months)

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
    
def get_num_workingdays(start_end)->int:
    return np.busday_count(np.datetime64('2021-01-01'), np.datetime64('2021-12-31'), holidays=const.HOLIDAYS)

