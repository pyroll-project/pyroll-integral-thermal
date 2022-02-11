import sys

from pyroll import RollPass, Transport


@RollPass.hookimpl
def contact_heat_transfer_coefficient(roll_pass: RollPass):
    """Backup implementation"""
    return 6


@Transport.hookimpl
def convection_heat_transfer_coefficient(transport: Transport):
    """Backup implementation"""
    return 1.5e-3


@Transport.hookimpl
def cooling_heat_transfer_coefficient(transport: Transport):
    """Backup implementation"""
    return 15e-3


@Transport.hookimpl
def relative_radiation_coefficient(transport: Transport):
    """Backup implementation"""
    return 0.8


RollPass.plugin_manager.register(sys.modules[__name__])
Transport.plugin_manager.register(sys.modules[__name__])
