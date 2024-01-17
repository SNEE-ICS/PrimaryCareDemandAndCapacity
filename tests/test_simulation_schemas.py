from ..src.simulation_schemas import AreaAppointmentTimeDistributions, AppointmentTimeDistributions, DidNotAttendRates, AreaDidNotAttendRates

# define the path to the sample yaml file from root
SAMPLE_APPOINTMENT_TIME_DISTRIBUTIONS_YAML_FILE:str = 'tests/sample_data/appointment-duration.yaml' 

def test_appointment_times_load_yaml():
    # load the yaml file
    location_distribution_dict = AreaAppointmentTimeDistributions.read_yaml(SAMPLE_APPOINTMENT_TIME_DISTRIBUTIONS_YAML_FILE)
    assert isinstance(location_distribution_dict, AreaAppointmentTimeDistributions)
    for k, v in location_distribution_dict.model_dump().items():
        assert isinstance(k, str)
        v_class = AppointmentTimeDistributions(**v) # convert the dictionary to a pydantic model
        assert isinstance(v_class, AppointmentTimeDistributions)
        for k1, v1 in v.items():
            assert isinstance(k1, str)
            assert isinstance(v1, list)
            for v2 in v1:
                assert isinstance(v2, float)


def test_did_not_attend_load_yaml():
    did_not_attend_rates =  DidNotAttendRates.read_yaml('tests/sample_data/dna-appointments.yaml')
    assert isinstance(did_not_attend_rates, DidNotAttendRates)
    for k, v in did_not_attend_rates.model_dump().items():
        assert isinstance(k, str)
        v_class = AreaDidNotAttendRates(**v)
        assert isinstance(v_class, AreaDidNotAttendRates)



    