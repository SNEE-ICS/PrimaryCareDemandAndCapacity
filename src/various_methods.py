import calendar
import numpy as np
import datetime as dt
import pandas as pd

import constants as const

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
            if the_date.isoweekday() and the_date not in const.ENGLAND_BANK_HOLIDAYS:
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

