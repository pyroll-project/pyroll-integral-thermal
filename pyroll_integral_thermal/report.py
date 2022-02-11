import sys

from pyroll import RollPass, Transport
from pyroll.ui.html_report.plugins import plugins, hookimpl


@hookimpl
def roll_pass_property(roll_pass: RollPass):
    return [
        ("temperature change", "{:.2g}".format(roll_pass.temperature_change)),
        ("temperature change by deformation", "{:.2g}".format(roll_pass.temperature_change_by_deformation)),
        ("temperature change by contact", "{:.2g}".format(roll_pass.temperature_change_by_contact)),
    ]


@hookimpl
def transport_property(transport: Transport):
    return [
        ("temperature change", "{:.2g}".format(transport.temperature_change)),
        ("temperature change by convection", "{:.2g}".format(transport.temperature_change_by_convection)),
        ("temperature change by cooling", "{:.2g}".format(transport.temperature_change_by_cooling)),
        ("temperature change by radiation", "{:.2g}".format(transport.temperature_change_by_radiation)),
    ]


plugins.register(sys.modules[__name__])
