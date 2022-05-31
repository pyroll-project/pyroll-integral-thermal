import sys

from pyroll.core import Transport

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

    common_factor = (
            transport.in_profile.cross_section.length * transport.duration / transport.in_profile.cross_section.area
            / (
                    (transport.in_profile.density + transport.out_profile.density)
                    * (transport.in_profile.thermal_capacity + transport.out_profile.thermal_capacity)
            ) * 2)

    mean_temperature = (transport.in_profile.temperature + 2 * transport.out_profile.temperature) / 3

    by_convection = -transport.convection_heat_transfer_coefficient * (
            mean_temperature - transport.atmosphere_temperature) * common_factor

    return by_convection


@Transport.hookimpl
def temperature_change_by_cooling(transport: Transport):
    if not hasattr(transport, "cooling_water_temperature"):
        return 0

    common_factor = (
            transport.in_profile.cross_section.length * transport.duration / transport.in_profile.cross_section.area
            / (
                    (transport.in_profile.density + transport.out_profile.density)
                    * (transport.in_profile.thermal_capacity + transport.out_profile.thermal_capacity)
            ) * 2)

    mean_temperature = (transport.in_profile.temperature + 2 * transport.out_profile.temperature) / 3

    by_cooling = -transport.cooling_heat_transfer_coefficient * (
            mean_temperature - transport.cooling_water_temperature) * common_factor

    return by_cooling


@Transport.hookimpl
def temperature_change_by_radiation(transport: Transport):
    if not hasattr(transport, "atmosphere_temperature"):
        return 0

    common_factor = (
            transport.in_profile.cross_section.length * transport.duration / transport.in_profile.cross_section.area
            / (
                    (transport.in_profile.density + transport.out_profile.density)
                    * (transport.in_profile.thermal_capacity + transport.out_profile.thermal_capacity)
            ) * 2)

    mean_temperature = (transport.in_profile.temperature + 2 * transport.out_profile.temperature) / 3

    by_radiation = -transport.relative_radiation_coefficient * stefan_boltzmann_coefficient * (
            mean_temperature ** 4 - transport.atmosphere_temperature ** 4) * common_factor

    return by_radiation


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
