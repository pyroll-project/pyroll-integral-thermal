import sys

from pyroll import Profile


@Profile.hookspec
def density(profile: Profile):
    """Get the density of the profile material."""


@Profile.hookspec
def thermal_capacity(profile: Profile):
    """Get the density of the profile material."""


Profile.plugin_manager.add_hookspecs(sys.modules[__name__])
Profile.plugin_manager.register(sys.modules[__name__])
