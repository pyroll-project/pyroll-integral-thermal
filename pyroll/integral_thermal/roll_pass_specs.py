from pyroll.core import RollPass, Hook

RollPass.deformation_heat_efficiency = Hook[float]()
"""Efficiency of heat generation through deformation. 1 means that all forming energy is dissipated as heat, 0 that all energy is saved in microstructure."""

RollPass.temperature_change_by_contact = Hook[float]()
"""Get the change in temperature by contact transfer within the roll pass."""

RollPass.temperature_change_by_deformation = Hook[float]()
"""Get the change in temperature by deformation heat within the roll pass."""

RollPass.temperature_change = Hook[float]()
"""Get the change in temperature within the roll pass."""

RollPass.Roll.contact_heat_transfer_coefficient = Hook[float]()
"""Get the heat transfer coefficient for contact of rolls and workpiece."""

RollPass.root_hooks.add(RollPass.OutProfile.temperature)
