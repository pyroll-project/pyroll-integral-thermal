import sys

from pyroll.core import RollPass
import numpy as np

from pyroll.integral_thermal.helper import mean_temperature, mean_density, mean_thermal_capacity


class RollImpls:
    @staticmethod
    @RollPass.Roll.hookimpl
    def temperature():
        """Default roll temperature at 293.15 K."""
        return 293.15

    @staticmethod
    @RollPass.Roll.hookimpl
    def contact_heat_transfer_coefficient():
        """Default implementation"""
        return 6e3


class OutProfileImpls:
    @staticmethod
    @RollPass.OutProfile.hookimpl
    def temperature(roll_pass: RollPass):
        return roll_pass.in_profile.temperature + roll_pass.temperature_change


class RollPassImpls:
    @staticmethod
    @RollPass.hookimpl
    def deformation_heat_efficiency(roll_pass: RollPass):
        """Default implementation"""
        return 0.95

    @staticmethod
    @RollPass.hookimpl
    def temperature_change_by_contact(roll_pass: RollPass):
        time = roll_pass.roll.contact_length / roll_pass.velocity
        return -(
                (
                        roll_pass.roll.contact_heat_transfer_coefficient
                        * (mean_temperature(roll_pass) - roll_pass.roll.temperature)
                        * time
                        * 2 * roll_pass.roll.contact_area
                ) / (
                        mean_density(roll_pass)
                        * mean_thermal_capacity(roll_pass)
                        * roll_pass.volume
                )
        )

    @staticmethod
    @RollPass.hookimpl
    def temperature_change_by_deformation(roll_pass: RollPass):
        deformation_resistance = (
            roll_pass.deformation_resistance
            if hasattr(roll_pass, "deformation_resistance")
            else (roll_pass.in_profile.flow_stress + 2 * roll_pass.out_profile.flow_stress) / 3
        )
        return (
                (
                        roll_pass.deformation_heat_efficiency
                        * deformation_resistance
                        * roll_pass.strain_change
                ) / (
                        mean_density(roll_pass)
                        * mean_thermal_capacity(roll_pass)
                )
        )

    @staticmethod
    @RollPass.hookimpl
    def temperature_change(roll_pass: RollPass):
        return roll_pass.temperature_change_by_contact + roll_pass.temperature_change_by_deformation


RollPass.plugin_manager.register(RollPassImpls)
RollPass.Roll.plugin_manager.register(RollImpls)
RollPass.OutProfile.plugin_manager.register(OutProfileImpls)
