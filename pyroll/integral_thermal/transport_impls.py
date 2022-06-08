import sys

from pyroll.core import Transport

from pyroll.integral_thermal.helper import mean_temperature, mean_density, mean_thermal_capacity

stefan_boltzmann_coefficient = 5.670374419e-8


@Transport.hookimpl
def convection_heat_transfer_coefficient(transport: Transport):
    """Backup implementation"""
    return 15


@Transport.hookimpl
def cooling_heat_transfer_coefficient(transport: Transport):
    """Backup implementation"""
    return 150


@Transport.hookimpl
def relative_radiation_coefficient(transport: Transport):
    """Backup implementation"""
    return 0.8


@Transport.hookimpl
def atmosphere_temperature(transport: Transport):
    """Backup atmosphere temperature at 293.15 K."""
    return 293.15


@Transport.hookimpl
def temperature_change_by_convection(transport: Transport):
    if not hasattr(transport, "atmosphere_temperature"):
        return 0

    return -(
            (
                    transport.convection_heat_transfer_coefficient
                    * (mean_temperature(transport) - transport.atmosphere_temperature)
                    * transport.in_profile.cross_section.length
                    * transport.duration
            ) / (
                    transport.in_profile.cross_section.area
                    * mean_density(transport)
                    * mean_thermal_capacity(transport)
            )
    )


@Transport.hookimpl
def temperature_change_by_cooling(transport: Transport):
    if not hasattr(transport, "cooling_water_temperature"):
        return 0

    return -(
            (
                    transport.cooling_heat_transfer_coefficient
                    * (mean_temperature(transport) - transport.cooling_water_temperature)
                    * transport.in_profile.cross_section.length
                    * transport.duration
            ) / (
                    transport.in_profile.cross_section.area
                    * mean_density(transport)
                    * mean_thermal_capacity(transport)
            )
    )


@Transport.hookimpl
def temperature_change_by_radiation(transport: Transport):
    if not hasattr(transport, "atmosphere_temperature"):
        return 0

    return -(
            (
                    transport.relative_radiation_coefficient
                    * stefan_boltzmann_coefficient
                    * (mean_temperature(transport) ** 4 - transport.atmosphere_temperature ** 4)
                    * transport.in_profile.cross_section.length
                    * transport.duration
            ) / (
                    transport.in_profile.cross_section.area
                    * mean_density(transport)
                    * mean_thermal_capacity(transport)
            )
    )


@Transport.hookimpl
def temperature_change(transport: Transport):
    return (
            transport.temperature_change_by_convection
            + transport.temperature_change_by_cooling
            + transport.temperature_change_by_radiation
    )


@Transport.OutProfile.hookimpl
def temperature(transport: Transport):
    return transport.in_profile.temperature + transport.temperature_change


Transport.plugin_manager.register(sys.modules[__name__])
Transport.OutProfile.plugin_manager.register(sys.modules[__name__])
