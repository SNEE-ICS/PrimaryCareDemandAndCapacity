<<<<<<< HEAD
<<<<<<< HEAD
from typing import Any, Dict, List, Union, TypeAlias, Type
import datetime as dt
=======
from typing import Dict, Iterable, List, Optional, Set, Tuple, Union, TypeAlias, Type
>>>>>>> e3f590a (moved conftest)
=======
from typing import Dict, Iterable, List, Optional, Set, Tuple, Union, TypeAlias, Type
>>>>>>> d371952 (resolving merge conflict)
from abc import ABC
import yaml
import random

from pydantic import (
    BaseModel,
    Field,
    RootModel,
    model_validator,
    ValidationError,
    create_model,
<<<<<<< HEAD
<<<<<<< HEAD
)

import pandas as pd
=======
    ConfigDict
)

import src.constants as constants   
>>>>>>> e3f590a (moved conftest)
=======
    ConfigDict
)

import src.constants as constants   
>>>>>>> d371952 (resolving merge conflict)

# this is used to define the arguments for the pydantic Field class
# so that probability of non attendance is between 0 and 1
PROPENSITY_FIELD_ARGS = {
    "default": 0.0,
    "ge": 0.0,
    "le": 1.0,
}

# this is used to confirm that the weights of a propensity sum to 1.0
PROPENSITY_ACCURACY_THRESHOLD = 0.001


class YamlLoader(ABC):
    """Protocol to define the methods that the yaml loader must implement"""

    @classmethod
    def read_yaml(cls, file_path: str):
        """
        Reads a YAML file and returns an instance of the class.

        Args:
            cls (type): The class to instantiate.
            file_path (str): The path to the YAML file.

        Returns:
            object: An instance of the class with attributes populated from the YAML file.
        """
        with open(file_path, "r") as f:
            yaml_data = yaml.safe_load(f)
            class_instance = cls(**yaml_data)
            return class_instance
        
class AreaModel(ABC):

    def get_area(self, area: str) -> Type[BaseModel]:
        """
        Get the propensity for a given area.

        Args:
            area (str): The area to get the details for.

        Returns:
            Dict[str, float]: The propensity for the given area.
        """
        return self.root.get(area)


<<<<<<< HEAD


class AreaModel(ABC):
    @property
    def areas(self) -> List[str]:
        """returns the list of areas"""
        return list(self.model_dump().keys())

    def get_area(self, area: str) -> Type[BaseModel]:
        """
        Get the propensity for a given area.

        Args:
            area (str): The area to get the details for.

        Returns:
            Dict[str, float]: The propensity for the given area.
        """
        return self.root.get(area)


class BaseChoice(BaseModel, ABC):
    """
    Base class for propensity choices, not to be used directly.
    The fields are the choices and the values are the probabilities.
    The sum of the field values must be 1.0.
    """

    @model_validator(mode="after")
    def check_sum(self):
        """Check that the propensity values sum to 1.0"""

        propensity_sum = sum(self.model_dump().values())
        # confirm the propensity values sum to 1.0
        if (
            propensity_sum > 1 + PROPENSITY_ACCURACY_THRESHOLD
            or propensity_sum < 1 - PROPENSITY_ACCURACY_THRESHOLD
        ):
            raise ValueError(f"Propensity values must sum to 1.0, got {propensity_sum}")
        return self

    def pick(self, n_choices: int = 1) -> Union[Any, List[Any]]:
        """
        Randomly selects one of the fields based on their probabilities (values must be float).

        Returns:
            str: The selected staff field name.
        """
        # get the probabilities as a dictionary
        probabilities_dict: Dict[str, float] = self.model_dump(by_alias=True)
        # randomly select a staff type based on the probabilities using the random module
        field_choices = random.choices(
            list(probabilities_dict.keys()),
            weights=list(probabilities_dict.values()),
            k=n_choices,
        )
        if n_choices == 1:
            return field_choices[0]
        else:
            return field_choices
=======
>>>>>>> d371952 (resolving merge conflict)


# using the pydantic Rootmodel to define a type alias/ schema
# this is essentially a dictionary structure with a key of type str and value of type int
<<<<<<< HEAD
<<<<<<< HEAD
_PopulationByYear = RootModel[Dict[int, int]]
=======
PopulationBaseline = create_model(
    "PopulationBaseline", **{k: (int, ...) for k in constants.GP_LIST_LABELS}
)
>>>>>>> e3f590a (moved conftest)
=======
PopulationBaseline = create_model(
    "PopulationBaseline", **{k: (int, ...) for k in constants.GP_LIST_LABELS}
)
>>>>>>> d371952 (resolving merge conflict)


class PopulationByYear(_PopulationByYear):
    @property
    def years(self) -> List[int]:
        """returns the list of years"""
        return list(self.model_dump.keys())

    def get_year(self, year: int):
        return self.root.get(year)


# then a dictionary keyed by year
_PopulationByAgeGroup = RootModel[Dict[str, PopulationByYear]]


class PopulationByAgeGroup(_PopulationByAgeGroup):
    @property
    def age_groups(self) -> List[str]:
        """returns the list of age_groups"""
        return list(self.model_dump().keys())

    def get_age_group(self, age_group: str) -> PopulationByYear:
        return self.root.get(age_group)


# then a dictionary keyed by area
# used for a populationEstimate by Area, note the leading underscore so not used directly
<<<<<<< HEAD
_PopulationByArea = RootModel[Dict[str, PopulationByAgeGroup]]


class PopulationByArea(_PopulationByArea, AreaModel):
    """Class to load and validate the population estimates by area"""

    def as_dataframe(
        self, proportions: bool = False, monthly: bool = False
    ) -> pd.DataFrame:
        """returns the population by area as a pandas dataframe"""
        # convert to dict
        df_ = pd.DataFrame.from_dict(self.model_dump(by_alias=True)).T

        # mangle the dataframe, empty list to hold rows
        mangled_rows = []
        # iterate over the rows
        for i, row in df_.iterrows():
            # iterate over the columns (age bands)
            for col in df_.columns:
                # each entry is a dictionary with the year as key and the population as value
                for k, v in row[col].items():
                    # append the row to the list
                    mangled_rows.append([col, i, k, v])
        pivot_df = pd.DataFrame(
            mangled_rows, columns=["age_band", "area", "year", "population"]
        ).pivot(index=["year", "area"], columns="age_band", values="population")

        if monthly:
            # add a month column to index
            expanded_index_df: pd.DataFrame = pd.DataFrame(
                index=pd.date_range(
                    dt.date(
                        pivot_df.index.get_level_values("year").min(), month=1, day=1
                    ),  # jan 1st of the first year
                    dt.date(
                        pivot_df.index.get_level_values("year").max(), month=12, day=1
                    ),  # dec 1st of the last year
                    freq="M",
                )  # month frequency
            ).assign(
                month=lambda df: df.index.month, year=lambda df: df.index.year
            )  # add month and year columns

            # add areas
            monthly_areas_df: pd.DataFrame = pd.concat(
                [
                    expanded_index_df.assign(area=area)
                    for area in df_.index.get_level_values("area").unique()
                ]
            ).set_index(["area", "year", "month"])
            del expanded_index_df  # free up memory
            # merge the two dataframes and interpolate the missing values
            monthly_population_df = monthly_areas_df.join(
                df_, how="outer"
            ).interpolate()

            if not proportions:
                return monthly_population_df
            else:
                return monthly_population_df.div(
                    monthly_population_df.sum(axis=1), axis=0
                )

        else:
            if not proportions:
                return pivot_df
            else:
                return pivot_df.div(pivot_df.sum(axis=1), axis=0)


_PopulationScenarios = RootModel[Dict[str, PopulationByArea]]


class PopulationScenarios(_PopulationScenarios, YamlLoader):
    """Class to load and validate the population scenarios yaml file for a yaml file of areas"""

    @property
    def scenarios(self) -> List[str]:
        """returns the list of scenarios"""
        return list(self.model_dump().keys())

    def get_scenario(self, scenario: str) -> PopulationByArea:
        """returns the population by area for a given scenario"""
        return self.root.get(scenario)


=======
_PopulationBaselineByArea = RootModel[Dict[str, PopulationBaseline]]


# subclassing the Rootmodel to add methods
class PopulationBaseLinesByArea(_PopulationBaselineByArea, AreaModel, YamlLoader):
    """Class to load and validate the population estimates yaml file for a yaml file of areas"""

    pass


# As above but for the population growth factors
PopulationGrowthFactors = create_model(
    "PopulationGrowthFactors", **{k: (float, ...) for k in constants.GP_LIST_LABELS}
)  # age group : growth factor

PopulationGrowthFactorsByArea = RootModel[
    Dict[str, PopulationGrowthFactors]
]  # area : PopulationGrowthFactors

_PopulationGrowthFactorScenarios = RootModel[
    Dict[str, PopulationGrowthFactorsByArea]
]  # scenario : PopulationGrowthFactorsByArea


class PopulationGrowthFactorScenarios(_PopulationGrowthFactorScenarios, YamlLoader):
    """Class to load and validate the population growth factor scenarios yaml file for a yaml file of areas"""

    pass


<<<<<<< HEAD
>>>>>>> e3f590a (moved conftest)
=======
>>>>>>> d371952 (resolving merge conflict)
# using the pydantic Rootmodel to define a type alias/ schema
# this is essentially a dictionary structure with a key of type str and iterable (list) of type float
AppointmentTimeDistributions = RootModel[Dict[str, List[float]]]


# Rootmodel used for subclassing, not to be used directly hence the leading underscore
_AreaAppointmentTimeDistributions = RootModel[Dict[str, AppointmentTimeDistributions]]


# subclassing the Rootmodel to add methods
class AreaAppointmentTimeDistributions(_AreaAppointmentTimeDistributions, YamlLoader):
    """Class to load and validate the appointment time distributions yaml file,
    fields can have any name"""

    pass


class StaffDidNotAttendRatesByDelivery(BaseModel):
    """
    Class to represent the did not attend rates for a given staff type
    """

    face_to_face: float = Field(alias="Face-to-Face", **PROPENSITY_FIELD_ARGS)
    home_visit: float = Field(alias="Home Visit", **PROPENSITY_FIELD_ARGS)
    telephone: float = Field(alias="Telephone", **PROPENSITY_FIELD_ARGS)
    unknown: float = Field(alias="Unknown", **PROPENSITY_FIELD_ARGS)
    video_online: float = Field(alias="Video/Online", **PROPENSITY_FIELD_ARGS)


class AreaDidNotAttendRates(BaseModel):
    """ "
    Class to represent the did not attend rates for a given area.
    The fields are the staff types and the values
    """

    gp: StaffDidNotAttendRatesByDelivery = Field(..., alias="GP", default_factory=dict)
    other: StaffDidNotAttendRatesByDelivery = Field(
        ..., alias="Other Practice staff", default_factory=dict
    )
    unknown: StaffDidNotAttendRatesByDelivery = Field(
        ..., alias="Unknown", default_factory=dict
    )


# not using the _ prefix here as this is just implementing the Rootmodel
_DidNotAttendRates = RootModel[Dict[str, AreaDidNotAttendRates]]


class DidNotAttendRatesByArea(_DidNotAttendRates, YamlLoader):
    """Class to load and validate the did not attend rates yaml file for a yaml file of areas"""

    pass


<<<<<<< HEAD
=======
class BaseChoice(BaseModel, ABC):
    """
    Base class for propensity choices, not to be used directly
    """

    pass

    @model_validator(mode="after")
    def check_sum(self):
        """Check that the propensity values sum to 1.0"""

        propensity_sum = sum(self.model_dump().values())
        # confirm the propensity values sum to 1.0
        if (
            propensity_sum > 1 + PROPENSITY_ACCURACY_THRESHOLD
            or propensity_sum < 1 - PROPENSITY_ACCURACY_THRESHOLD
        ):
            raise ValueError(f"Propensity values must sum to 1.0, got {propensity_sum}")
        return self


>>>>>>> e3f590a (moved conftest)
class AppointmentStaffChoice(BaseChoice):
    """
    Class to represent the propensity of a given staff type for appointments
    """

    gp: float = Field(alias="GP", **PROPENSITY_FIELD_ARGS)
    other: float = Field(alias="Other Practice staff", **PROPENSITY_FIELD_ARGS)
    unknown: float = Field(alias="Unknown", **PROPENSITY_FIELD_ARGS)

<<<<<<< HEAD
<<<<<<< HEAD

# not using the _ prefix here as this is just implementing the Rootmodel
_StaffTypePropensityByArea = RootModel[Dict[str, AppointmentStaffChoice]]


class StaffTypePropensityByArea(_StaffTypePropensityByArea, YamlLoader, AreaModel):
    """Class to load and validate the staff type propensity yaml file for a yaml file of areas"""

    pass
=======
=======
>>>>>>> d371952 (resolving merge conflict)
    def pick_staff_type(self) -> str:
        """
        Randomly selects a staff type based on the given probabilities.

        Returns:
            str: The selected staff type.
        """
        # get the probabilities as a dictionary
        probabilities_dict: Dict[str, float] = self.model_dump(by_alias=True)
        # randomly select a staff type based on the probabilities using the random modu` oi,m1¦¦\le
        staff_type = random.choices(
            list(probabilities_dict.keys()),
            weights=list(probabilities_dict.values()),
            k=1,
        )[0]
        # return the selected staff type
        return staff_type

_StaffTypePropensityByArea = RootModel[Dict[str, AppointmentStaffChoice]]

class StaffTypePropensityByArea(_StaffTypePropensityByArea, YamlLoader):
    """Class to load and validate the did not attend rates yaml file for a yaml file of areas"""
    def get(self, area: str) -> AppointmentStaffChoice:
        """
        Get the propensity for a given area.

        Args:
            area (str): The area to get the propensity for.

        Returns:
            AppointmentStaffChoice: The propensity for the given area.
        """
        return self.root.get(area)


<<<<<<< HEAD
>>>>>>> e3f590a (moved conftest)

=======
>>>>>>> d371952 (resolving merge conflict)

class AppointmentDeliveryChoice(BaseChoice):
    """
    Class to represent the propensity of a given delivery type for appointments
    """

    face_to_face: float = Field(alias="Face-to-Face", **PROPENSITY_FIELD_ARGS)
    home_visit: float = Field(alias="Home Visit", **PROPENSITY_FIELD_ARGS)
    telephone: float = Field(alias="Telephone", **PROPENSITY_FIELD_ARGS)
    unknown: float = Field(alias="Unknown", **PROPENSITY_FIELD_ARGS)
    video_online: float = Field(alias="Video/Online", **PROPENSITY_FIELD_ARGS)

    def pick_delivery_type(self) -> str:
        """
        Randomly selects a delivery type based on the given probabilities.

        Returns:
            str: The selected delivery type.
        """
        # get the probabilities as a dictionary
        probabilities_dict: Dict[str, float] = self.model_dump(by_alias=True)

        # randomly select a staff type based on the probabilities using the random module
        delivery_type = random.choices(
            list(probabilities_dict.keys()),
            weights=list(probabilities_dict.values()),
            k=1,
        )[0]
        # return the selected staff type
        return delivery_type


<<<<<<< HEAD
<<<<<<< HEAD
class DeliveryPropensityByStaff(BaseModel):
    gp: AppointmentDeliveryChoice = Field(alias="GP")
    other: AppointmentDeliveryChoice = Field(alias="Other Practice staff")
    unknown: AppointmentDeliveryChoice = Field(alias="Unknown")
=======
=======
>>>>>>> d371952 (resolving merge conflict)
class DeliveryPropensityByStaff(BaseChoice):
    gp: AppointmentDeliveryChoice = Field(alias="GP", **PROPENSITY_FIELD_ARGS)
    other: AppointmentDeliveryChoice = Field(alias="Other Practice staff", **PROPENSITY_FIELD_ARGS)
    unknown: AppointmentDeliveryChoice = Field(alias="Unknown", **PROPENSITY_FIELD_ARGS)
<<<<<<< HEAD
>>>>>>> e3f590a (moved conftest)
=======
>>>>>>> d371952 (resolving merge conflict)


_DeliveryPropensityByArea = RootModel[Dict[str, DeliveryPropensityByStaff]]


class DeliveryPropensityByArea(_DeliveryPropensityByArea, YamlLoader):
    """Class to load and validate the did not attend rates yaml file for a yaml file of areas"""
<<<<<<< HEAD
<<<<<<< HEAD

    pass
=======
    pass
>>>>>>> e3f590a (moved conftest)
=======
    pass
>>>>>>> d371952 (resolving merge conflict)
