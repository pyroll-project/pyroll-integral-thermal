import sys

from pyroll.core import RollPass


@RollPass.Roll.hookspec
def temperature(roll: RollPass.Roll, roll_pass: RollPass):
    """Get the mean temperature of the working rolls."""


@RollPass.Roll.hookspec
def contact_heat_transfer_coefficient(roll: RollPass.Roll, roll_pass: RollPass):
    """Get the heat transfer coefficient for contact of rolls and workpiece."""


RollPass.Roll.plugin_manager.add_hookspecs(sys.modules[__name__])
