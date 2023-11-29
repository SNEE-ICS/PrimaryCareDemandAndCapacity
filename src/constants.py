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


# Location for outputs
NOTEBOOK_OUTPUT_BASE_PATH = "../outputs/"
NOTEBOOK_OUTPUT_TABLES_PATH = NOTEBOOK_OUTPUT_BASE_PATH + "tables/"
NOTEBOOK_OUTPUT_FIGURES_PATH = NOTEBOOK_OUTPUT_BASE_PATH + "figures/"
SIMULATION_RESULTS_PATH = NOTEBOOK_OUTPUT_BASE_PATH + "simulation_results/"

