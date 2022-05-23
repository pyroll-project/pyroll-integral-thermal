import sys

from pyroll.core import Unit
from pyroll.ui import Exporter


@Exporter.hookimpl
def columns(unit: Unit):
    return dict(
        in_temperature=unit.in_profile.temperature,
        out_temperature=unit.out_profile.temperature
    )


Exporter.plugin_manager.register(sys.modules[__name__])
