import numpy as np

from pyroll_integral_thermal.roll_pass_impls import temperature_change_by_contact


class DummyProfile:
    def __init__(self):
        self.cross_section = 1
        self.density = 1
        self.thermal_capacity = 1


class DummyRollPass:
    def __init__(self):
        self.in_profile = DummyProfile()
        self.in_profile.cross_section = 3
        self.out_profile = DummyProfile()
        self.contact_length = 1
        self.contact_area = 1
        self.velocity = 1
        self.contact_heat_transfer_coefficient = 1
        self.mean_temperature = 2
        self.roll_temperature = 1


def test_contact():
    rp = DummyRollPass()

    dT = temperature_change_by_contact(rp)

    assert np.isclose(dT, -0.5)


def test_contact_velocity_change():
    rp = DummyRollPass()

    dT1 = temperature_change_by_contact(rp)

    rp.velocity = 2
    dT2 = temperature_change_by_contact(rp)

    rp.velocity = 0.5
    dT3 = temperature_change_by_contact(rp)

    assert -dT1 > -dT2
    assert -dT3 > -dT1
