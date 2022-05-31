import sys

from pyroll.core import RollPass
import numpy as np


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
        volume = roll_pass.roll.contact_length / 3 * (roll_pass.in_profile.cross_section.area + roll_pass.out_profile.cross_section.area + np.sqrt(
            roll_pass.in_profile.cross_section.area * roll_pass.out_profile.cross_section.area))
        area_volume_ratio = roll_pass.roll.contact_area * 2 / volume
        time = roll_pass.roll.contact_length / roll_pass.velocity
        denominator = (
                              (roll_pass.in_profile.density + roll_pass.out_profile.density)
                              * (roll_pass.in_profile.thermal_capacity + roll_pass.out_profile.thermal_capacity)
                      ) / 2
        by_contact = -(
                roll_pass.roll.contact_heat_transfer_coefficient * (
                roll_pass.in_profile.temperature - roll_pass.roll.temperature)
                * time * area_volume_ratio
        ) / denominator

        return by_contact

    @staticmethod
    @RollPass.hookimpl
    def temperature_change_by_deformation(roll_pass: RollPass):
        deformation_resistance = (
            roll_pass.deformation_resistance
            if hasattr(roll_pass, "deformation_resistance")
            else (roll_pass.in_profile.flow_stress + 2 * roll_pass.out_profile.flow_stress) / 3
        )
        denominator = (
                              (roll_pass.in_profile.density + roll_pass.out_profile.density)
                              * (roll_pass.in_profile.thermal_capacity + roll_pass.out_profile.thermal_capacity)
                      ) / 2
        by_deformation = roll_pass.deformation_heat_efficiency * deformation_resistance * roll_pass.strain_change / denominator

        return by_deformation

    @staticmethod
    @RollPass.hookimpl
    def temperature_change(roll_pass: RollPass):
        return roll_pass.temperature_change_by_contact + roll_pass.temperature_change_by_deformation


RollPass.plugin_manager.register(RollPassImpls)
RollPass.Roll.plugin_manager.register(RollImpls)
RollPass.OutProfile.plugin_manager.register(OutProfileImpls)
