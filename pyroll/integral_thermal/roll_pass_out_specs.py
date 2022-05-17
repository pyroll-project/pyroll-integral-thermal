import sys

from pyroll.core import RollPass


@RollPass.OutProfile.hookspec
def temperature(roll_pass, profile):
    """Get the temperature of the out profile."""


RollPass.OutProfile.plugin_manager.add_hookspecs(sys.modules[__name__])
RollPass.OutProfile.root_hooks.add("temperature")
