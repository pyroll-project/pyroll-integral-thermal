from pyroll.core.grooves import SquareGroove, DiamondGroove, CircularOvalGroove, RoundGroove
from pyroll.core import Profile
from pyroll.core import RollPass
from pyroll.core import Transport
from numpy import pi

# initial profile
in_profile = Profile(
    width=68e-3,
    height=68e-3,
    groove=SquareGroove(r1=0, r2=3e-3, tip_angle=pi / 2, tip_depth=34e-3),
    temperature=1200 + 273.15,
    strain=0,
    density=7e3,
    thermal_capacity=630,
    material="S355J2",
    flow_stress=50e6
)

# pass sequence
sequence = [
    RollPass(
        label="Raute I",
        groove=DiamondGroove(
            usable_width=76.55e-3,
            tip_depth=22.1e-3,
            r1=12e-3,
            r2=8e-3
        ),
        roll_radius=260e-3,
        roll_temperature=303,
        velocity=1.4,
        gap=3e-3,
        geuze_coefficient=0.3,
    ),
    Transport(
        time=1
    ),
    RollPass(
        label="Quadrat II",
        groove=SquareGroove(
            usable_width=52.7e-3,
            tip_depth=25.95e-3,
            r1=8e-3,
            r2=6e-3
        ),
        roll_radius=260e-3,
        roll_temperature=303,
        velocity=1.4,
        gap=3e-3,
        geuze_coefficient=0.3,
    ),
]
