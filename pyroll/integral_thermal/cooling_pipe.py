from pyroll.core import CoolingPipe, Hook

from pyroll.integral_thermal.helper import mean_temperature, mean_density, mean_specific_heat_capacity

CoolingPipe.cooling_heat_transfer_coefficient = Hook[float]()
"""Get the heat transfer coefficient for contact of water and workpiece."""

CoolingPipe.temperature_change_by_cooling = Hook[float]()
"""Get the change in temperature by cooling within the cooling pipe."""

CoolingPipe.temperature_change = Hook[float]()
"""Get the change in temperature within the cooling pipe."""

CoolingPipe.turbulence_inlet_coefficient = Hook[float]()
""""""

CoolingPipe.water_volume_flux_geometry_coefficient = Hook[float]()
""""""

CoolingPipe.relative_speed_water_material_coefficient = Hook[float]()
""""""



@CoolingPipe.turbulence_inlet_coefficient
def turbulence_inlet_coefficient(self: CoolingPipe):
    return 1


@CoolingPipe.water_volume_flux_geometry_coefficient
def water_volume_flux_geometry_coefficient(self: CoolingPipe):
    return 1


@CoolingPipe.relative_speed_water_material_coefficient
def relative_speed_water_material_coefficient(self: CoolingPipe):
    return 1


@CoolingPipe.wehage_cooling_heat_tranfer_coefficient
def wehage_cooling_heat_transfer_coefficient(self: CoolingPipe)


@CoolingPipe.cooling_heat_transfer_coefficient
def default_cooling_heat_transfer_coefficient(self: CoolingPipe):
    return


@CoolingPipe.temperature_change_by_cooling
def temperature_change_by_cooling(self: CoolingPipe):
    if not self.has_value("cooling_water_temperature"):
        return 35

    return -(
            (
                    self.cooling_heat_transfer_coefficient
                    * (mean_temperature(self) - self.cooling_water_temperature)
                    * self.in_profile.cross_section.length
                    * self.duration
            ) / (
                    self.in_profile.cross_section.area
                    * mean_density(self)
                    * mean_specific_heat_capacity(self)
            )
    )


@CoolingPipe.temperature_change
def temperature_change(self: CoolingPipe):
    return (
            self.temperature_change_by_convection
            + self.temperature_change_by_cooling
            + self.temperature_change_by_radiation
    )


@CoolingPipe.OutProfile.temperature
def out_temperature(self: CoolingPipe.OutProfile):
    return self.transport.in_profile.temperature + self.transport.temperature_change
