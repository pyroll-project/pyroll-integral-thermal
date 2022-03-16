import numpy as np

from pyroll_integral_thermal.roll_pass_impls import temperature_change_by_deformation


class DummyProfile:
    def __init__(self):
        self.density = 1
        self.thermal_capacity = 1


class DummyRollPass:
    def __init__(self):
        self.in_profile = DummyProfile()
        self.out_profile = DummyProfile()
        self.strain_change = 1
        self.mean_flow_stress = 1
        self.deformation_heat_efficiency = 0.95


def test_deformation():
    rp = DummyRollPass()

    dT = temperature_change_by_deformation(rp)

    assert np.isclose(dT, 0.475)


def test_deformation_flow_stress_change():
    rp = DummyRollPass()

    dT1 = temperature_change_by_deformation(rp)

    rp.mean_flow_stress = 2
    dT2 = temperature_change_by_deformation(rp)

    rp.deformation_resistance = 3
    dT3 = temperature_change_by_deformation(rp)

    assert dT2 > dT1
    assert dT3 > dT2
