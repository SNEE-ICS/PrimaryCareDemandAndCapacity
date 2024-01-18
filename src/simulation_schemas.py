from typing import Dict, Iterable, List, Optional, Set, Tuple, Union, TypeAlias, Type
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
    ConfigDict
)

import src.constants as constants   

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




# using the pydantic Rootmodel to define a type alias/ schema
# this is essentially a dictionary structure with a key of type str and value of type int
PopulationBaseline = create_model(
    "PopulationBaseline", **{k: (int, ...) for k in constants.GP_LIST_LABELS}
)

# used for a populationEstimate by Area, note the leading underscore so not used directly
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


class AppointmentStaffChoice(BaseChoice):
    """
    Class to represent the propensity of a given staff type for appointments
    """

    gp: float = Field(alias="GP", **PROPENSITY_FIELD_ARGS)
    other: float = Field(alias="Other Practice staff", **PROPENSITY_FIELD_ARGS)
    unknown: float = Field(alias="Unknown", **PROPENSITY_FIELD_ARGS)

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


class DeliveryPropensityByStaff(BaseChoice):
    gp: AppointmentDeliveryChoice = Field(alias="GP", **PROPENSITY_FIELD_ARGS)
    other: AppointmentDeliveryChoice = Field(alias="Other Practice staff", **PROPENSITY_FIELD_ARGS)
    unknown: AppointmentDeliveryChoice = Field(alias="Unknown", **PROPENSITY_FIELD_ARGS)


_DeliveryPropensityByArea = RootModel[Dict[str, DeliveryPropensityByStaff]]


class DeliveryPropensityByArea(_DeliveryPropensityByArea, YamlLoader):
    """Class to load and validate the did not attend rates yaml file for a yaml file of areas"""
    pass