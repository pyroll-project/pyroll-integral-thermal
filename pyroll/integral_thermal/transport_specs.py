from pyroll.core import Transport, Hook

Transport.cooling_water_temperature = Hook[float]()
"""Get the temperature of the cooling water."""

Transport.convection_heat_transfer_coefficient = Hook[float]()
"""Get the heat transfer coefficient for contact of rolls and workpiece."""

Transport.cooling_heat_transfer_coefficient = Hook[float]()
"""Get the heat transfer coefficient for contact of rolls and workpiece."""

Transport.relative_radiation_coefficient = Hook[float]()
"""Get the heat transfer coefficient for contact of rolls and workpiece."""

Transport.temperature_change_by_convection = Hook[float]()
"""Get the change in temperature by convection within the transport."""

Transport.temperature_change_by_cooling = Hook[float]()
"""Get the change in temperature by cooling within the transport."""

Transport.temperature_change_by_radiation = Hook[float]()
"""Get the change in temperature by radiation within the transport."""

Transport.temperature_change = Hook[float]()
"""Get the change in temperature within the transport."""

Transport.root_hooks.add(Transport.OutProfile.temperature)
