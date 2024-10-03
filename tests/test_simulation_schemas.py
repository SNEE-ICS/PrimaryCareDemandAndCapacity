import pytest
from pydantic import ValidationError
from src.simulation_schemas import (
    AreaAppointmentTimeDistributions, 
    AppointmentTimeDistributions, 
    DidNotAttendRatesByArea, 
    AreaDidNotAttendRates, 
    StaffPropensityByArea, 
    AppointmentStaffChoice,
    DeliveryPropensityByArea,
    PopulationScenarios
)

# define the path to the sample yaml file from root
SAMPLE_APPOINTMENT_TIME_DISTRIBUTIONS_YAML_FILE: str = (
    "tests/sample_data/appointment-duration.yaml"
)


def test_appointment_times_load_yaml():

    """Test that the yaml file can be loaded"""
    # load the yaml file
    location_distribution_dict = AreaAppointmentTimeDistributions.read_yaml(
        SAMPLE_APPOINTMENT_TIME_DISTRIBUTIONS_YAML_FILE
    )
    # assert that it is the correct instance
    assert isinstance(location_distribution_dict, AreaAppointmentTimeDistributions)
    # iterate though the model
    for k, v in location_distribution_dict.model_dump().items():
        # check the key is str
        assert isinstance(k, str)
        # construct the class from dictionary
        v_class = AppointmentTimeDistributions(**v)  
        # convert the dictionary to a pydantic model
        assert isinstance(v_class, AppointmentTimeDistributions)
        # iterate through the subclass
        for k1, v1 in v.items():
            assert isinstance(k1, str)
            assert isinstance(v1, list)
            for v2 in v1:
                assert isinstance(v2, float)


def test_did_not_attend_load_yaml():
    did_not_attend_rates = DidNotAttendRatesByArea.read_yaml(
        "tests/sample_data/dna-appointments.yaml"
    )
    assert isinstance(did_not_attend_rates, DidNotAttendRatesByArea)
    for k, v in did_not_attend_rates.model_dump().items():
        assert isinstance(k, str)
        v_class = AreaDidNotAttendRates(**v)
        assert isinstance(v_class, AreaDidNotAttendRates)


def test_staff_propensity_yaml():
    staff_propensity = StaffPropensityByArea.read_yaml(
        "tests/sample_data/staff_propensity.yaml"
    )
    assert isinstance(staff_propensity, StaffPropensityByArea)


def test_staff_propensity_yaml_raises_error():
    """This will error as the sum is gt 1"""
    with pytest.raises(Exception):
        StaffPropensityByArea.read_yaml(
            "tests/sample_data/staff_propensity_error.yaml"
        )

def test_staff_propensity_pick():
    staff_propensity = StaffPropensityByArea.read_yaml(
        "tests/sample_data/staff_propensity.yaml"
    )
    # get areas
    for area in staff_propensity.areas:
        area_propensity:AppointmentStaffChoice = staff_propensity.get_area(area)
        assert isinstance(area_propensity, AppointmentStaffChoice)
        # pick one
        staff_type:str = area_propensity.pick()
        assert isinstance(staff_type, str)
        assert staff_type in ["GP", "Other Practice staff", "Unknown"]
    areas = list(staff_propensity.model_dump().keys())
    assert isinstance(staff_propensity, StaffPropensityByArea)
    staff_type = staff_propensity.get_area(areas[0]).pick()
    assert isinstance(staff_type, str)


def test_appt_mode_propensity():
    appt_mode_propensity = DeliveryPropensityByArea.read_yaml(
        "tests/sample_data/appt_mode_propensity.yaml"
    )
    assert isinstance(appt_mode_propensity, DeliveryPropensityByArea)


def test_appt_mode_propensity_raises_error():
    """This will error as the sum is gt 1"""
    with pytest.raises(ValidationError):
        DeliveryPropensityByArea.read_yaml(
            "tests/sample_data/appt_mode_propensity_error.yaml"
        )
        
def test_population_yamls():
    population = PopulationScenarios.read_yaml("tests/sample_data/population_projection.yaml")
    assert isinstance(population, PopulationScenarios)
        
def test_population_yaml_raises_error():
    with pytest.raises(ValidationError):
        PopulationScenarios.read_yaml("tests/sample_data/appt_mode_propensity_error.yaml")
