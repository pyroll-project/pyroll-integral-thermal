import sys

from pyroll.core import Transport

from pyroll.integral_thermal.helper import mean_temperature, mean_density, mean_thermal_capacity

stefan_boltzmann_coefficient = 5.670374419e-8


@Transport.convection_heat_transfer_coefficient
def default_convection_heat_transfer_coefficient(self: Transport):
    return 15


@Transport.cooling_heat_transfer_coefficient
def default_cooling_heat_transfer_coefficient(self: Transport):
    return 150


@Transport.relative_radiation_coefficient
def default_relative_radiation_coefficient(self: Transport):
    return 0.8


@Transport.environment_temperature
def default_environment_temperature(self: Transport):
    """Backup atmosphere temperature at 293.15 K."""
    return 293.15


@Transport.temperature_change_by_convection
def temperature_change_by_convection(self: Transport):
    if not self.has_value("environment_temperature"):
        return 0

    return -(
            (
                    self.convection_heat_transfer_coefficient
                    * (mean_temperature(self) - self.environment_temperature)
                    * self.in_profile.cross_section.length
                    * self.duration
            ) / (
                    self.in_profile.cross_section.area
                    * mean_density(self)
                    * mean_thermal_capacity(self)
            )
    )


@Transport.temperature_change_by_cooling
def temperature_change_by_cooling(self: Transport):
    if not self.has_value("cooling_water_temperature"):
        return 0

    return -(
            (
                    self.cooling_heat_transfer_coefficient
                    * (mean_temperature(self) - self.cooling_water_temperature)
                    * self.in_profile.cross_section.length
                    * self.duration
            ) / (
                    self.in_profile.cross_section.area
                    * mean_density(self)
                    * mean_thermal_capacity(self)
            )
    )


@Transport.temperature_change_by_radiation
def temperature_change_by_radiation(self: Transport):
    if not self.has_value("environment_temperature"):
        return 0

    return -(
            (
                    self.relative_radiation_coefficient
                    * stefan_boltzmann_coefficient
                    * (mean_temperature(self) ** 4 - self.environment_temperature ** 4)
                    * self.in_profile.cross_section.length
                    * self.duration
            ) / (
                    self.in_profile.cross_section.area
                    * mean_density(self)
                    * mean_thermal_capacity(self)
            )
    )


@Transport.temperature_change
def temperature_change(self: Transport):
    return (
            self.temperature_change_by_convection
            + self.temperature_change_by_cooling
            + self.temperature_change_by_radiation
    )


@Transport.OutProfile.temperature
def out_temperature(self: Transport.OutProfile):
    return self.transport().in_profile.temperature + self.transport().temperature_change
