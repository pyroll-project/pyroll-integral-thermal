import sys

from pyroll.core import Transport


@Transport.OutProfile.hookspec
def temperature(transport):
    """Get the temperature of the out profile."""


Transport.OutProfile.plugin_manager.add_hookspecs(sys.modules[__name__])
Transport.OutProfile.root_hooks.add("temperature")
