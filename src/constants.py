from typing import Final, Dict, NamedTuple, Type
import datetime as dt
import holidays


# NHS ENGLAND APPOINTMENTS
REGIONAL_DATA_ZIP: Final[str] = "https://files.digital.nhs.uk/3D/ED1EDE/Appointments_GP_Regional_CSV_Aug_23.zip"
# CSV OF INTEREST
SNEE_CSV: Final[str] = "/content/Regional_CSV_SuffolkNEEssex.csv"

# ONS DATA
SUBNATIONAL_ONS_ZIP: Final[str] = "https://www.ons.gov.uk/file?uri=/peoplepopulationandcommunity/populationandmigration/populationprojections/datasets/localauthoritiesinenglandz1/2018based/2018snpppopulation.zip"
# Dictionary of ONS CSVs
ONS_CSVS: Final[Dict[str, str]] = {
    k: f"/content/2018 SNPP Population {k}.csv" for k in ['males', 'females', 'persons']}

# BANK HOLIDAYS
ENGLAND_BANK_HOLIDAYS: Final[Type[Dict[dt.date, str]]] = holidays.UnitedKingdom(
    years=[i for i in range(2021, 2035)])

# SUB ICB AREAS
IPS_EAST_SUFF = "Ipswich & East Suffolk"
WEST_SUFF = "West Suffolk"
NE_ESSEX = "North East Essex"

# SUB ICB CODES
SUB_ICB_CODES = {"06L": IPS_EAST_SUFF,
                 "07K": WEST_SUFF,
                 "06T": NE_ESSEX}

# ONS CODE
ONS_CODES = {"E38000086": IPS_EAST_SUFF,
                 "E38000204": WEST_SUFF,
                 "E38000117": NE_ESSEX}

# CCG to sub-ICB
CCG_SUB_ICB = {"NHS Ipswich and East Suffolk CCG": IPS_EAST_SUFF,
               "NHS West Suffolk CCG": WEST_SUFF,
               "NHS North East Essex CCG": NE_ESSEX}

# ONS TO SUB-ICB
ICB_ONS_AREAS = {"Tendring": NE_ESSEX,
                 "Colchester": NE_ESSEX,
                 "Forest Heath": WEST_SUFF,
                 "St Edmundsbury": WEST_SUFF,
                 "Babergh": IPS_EAST_SUFF,
                 "Mid Suffolk": IPS_EAST_SUFF,
                 "Suffolk Coastal": IPS_EAST_SUFF,
                 "Ipswich": IPS_EAST_SUFF}

#ORG Code
ORG_CODE = {'QJG': 'NHS SUFFOLK AND NORTH EAST ESSEX INTEGRATED CARE BOARD'}

# Location for outputs
# these are all relative to the repo root directory ! 
NOTEBOOK_OUTPUT_BASE_PATH = "outputs/"
NOTEBOOK_OUTPUT_TABLES_PATH = NOTEBOOK_OUTPUT_BASE_PATH + "tables/"
NOTEBOOK_OUTPUT_FIGURES_PATH = NOTEBOOK_OUTPUT_BASE_PATH + "plots/"
SIMULATION_RESULTS_PATH = NOTEBOOK_OUTPUT_BASE_PATH + "simulation_results/"


ONS_POPULATION_SCENARIOS_NAME = "ONS Population projections by single year of age mid-2018 to mid-2043"

<<<<<<< HEAD
GP_LIST_AGE_BANDS = [i for i in range(-1,90,5)] + [float('inf')] # -1, 4, 9, ... 84, 89, inf used for pd.cut()
GP_LIST_LABELS = [f"{i+1}-{i+5}" for i in GP_LIST_AGE_BANDS[:-2]] + ["90+"] # 0-4, 5-9, ... 85-89, 90+

=======
>>>>>>> 6cb25f3 (updated data catalog, function to get staff_type dict and dict from excel in constant.py)
STAFF_TYPE = {  "Advanced Nurse Practitioners": "Nurses",
                "Advanced Occupational Therapist Practitioners": "Direct Patient Care",
                "Advanced Paramedic Practitioners": "Direct Patient Care",
                "Advanced Pharmacist Practitioners": "Direct Patient Care",
                "Advanced Physiotherapist Practitioners": "Direct Patient Care",
                "Dieticians": "Direct Patient Care",
                "Dispensers": "Direct Patient Care",
                "Estates and Ancillary": "Admin/Non-Clinical",
                "Extended Role Practice Nurses": "Nurses",
                "GP Partners": "GP",
                "GP Regular Locums": "GP",
                "GP Retainers": "GP",
                "GPs in Training Grades": "GP",
                "General Practice Assistants": "Direct Patient Care",
                "Health Support Workers": "Direct Patient Care",
                "Healthcare Assistants": "Direct Patient Care",
                "IAPT Staff": "Direct Patient Care",
                "Management Partners": "Admin/Non-Clinical",
                "Managers": "Admin/Non-Clinical",
                "Medical Secretaries": "Admin/Non-Clinical",
                "Nurse Dispensers": "Nurses",
                "Nurse Specialists": "Nurses",
                "Nursing Associates": "Direct Patient Care",
                "Nursing Partners": "Nurses",
                "Other Admin/Non-clinical": "Admin/Non-Clinical",
                "Other Direct Patient Care": "Direct Patient Care",
                "Other Nurses": "Nurses",
                "Paramedics": "Direct Patient Care",
                "Pharmacists": "Direct Patient Care",
                "Pharmacy Technicians": "Direct Patient Care",
                "Phlebotomists": "Direct Patient Care",
                "Physician Associates": "Direct Patient Care",
                "Physiotherapists": "Direct Patient Care",
                "Podiatrists": "Direct Patient Care",
                "Practice Nurses": "Nurses",
                "Receptionists": "Admin/Non-Clinical",
                "Salaried GPs": "GP",
                "Social Prescribing Link Workers": "Direct Patient Care",
                "Telephonists": "Admin/Non-Clinical",
                "Therapists": "Direct Patient Care",
                "Trainee Nurses":"Nurses",
                "Trainee Nursing Associates": "Direct Patient Care"
            }

GP_LIST_AGE_BANDS = [i for i in range(-1,90,5)] + [float('inf')] # -1, 4, 9, ... 84, 89, inf used for pd.cut()
GP_LIST_LABELS = [f"{i+1}-{i+5}" for i in GP_LIST_AGE_BANDS[:-2]] + ["90+"] # 0-4, 5-9, ... 85-89, 90+

