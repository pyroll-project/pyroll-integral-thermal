from pyroll.core.grooves import SquareGroove, DiamondGroove, CircularOvalGroove, RoundGroove
from pyroll.core import Profile
from pyroll.core import RollPass
from pyroll.core import Transport
from numpy import pi

# initial profile
in_profile = Profile(
    width=68,
    height=68,
    groove=SquareGroove(r1=0, r2=3, tip_angle=pi / 2, tip_depth=34),
    temperature=1200 + 273.15,
    strain=0,
    density=7e-3,
    thermal_capacity=630,
    thermal_conductivity=25,
    thermal_expansion_coefficient=1.2e-5,
    geuze_coefficient=0.3,
    material="S355J2",
    mean_grain_size=50,
    flow_stress=50
)


# pass sequence
sequence = [
    RollPass(
        label="Raute I",
        groove=DiamondGroove(
            usable_width=76.55,
            tip_depth=(47.2 - 3) / 2,
            r1=12,
            r2=8
        ),
        in_profile_rotation=0,
        roll_radius=200,
        roll_temperature=303,
        velocity=50e3,
        gap=3
    ),
    Transport(
        time=5,
        atmosphere_temperature=293,
        convection_heat_transfer_coefficient=15e-3,
        cooling_heat_transfer_coefficient=0,
        cooling_water_temperature=0,
        relative_radiation_coefficient=0.8
    ),
    RollPass(
        label="Quadrat II",
        groove=SquareGroove(
            usable_width=52.7,
            tip_depth=(54.9 - 3) / 2,
            r1=8,
            r2=6
        ),
        in_profile_rotation=90,
        roll_radius=200,
        roll_temperature=303,
        velocity=50e3,
        gap=3
    ),
]
