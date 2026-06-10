"""Event platform for the TOTO Washlet integration."""

from __future__ import annotations

import logging

from homeassistant.components.event import EventEntity
from homeassistant.components.infrared import (
    InfraredReceivedSignal,
    InfraredReceiverConsumerEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .commands import TotoWashletCode
from .const import CONF_INFRARED_RECEIVER_ENTITY_ID
from .entity import TotoWashletEntity

_LOGGER = logging.getLogger(__name__)

PARALLEL_UPDATES = 0

_COMMAND_CODE_TO_EVENT_TYPE: dict[TotoWashletCode, str] = {
    code: code.name.lower() for code in TotoWashletCode
}
_EVENT_TYPE_UNKNOWN = "unknown"
_EVENT_TYPES = [*_COMMAND_CODE_TO_EVENT_TYPE.values(), _EVENT_TYPE_UNKNOWN]


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up TOTO Washlet event entity from a config entry."""
    if not (
        receiver_entity_id := entry.options.get(
            CONF_INFRARED_RECEIVER_ENTITY_ID,
            entry.data.get(CONF_INFRARED_RECEIVER_ENTITY_ID),
        )
    ):
        return

    async_add_entities([TotoWashletReceivedCommandEvent(entry, receiver_entity_id)])


class TotoWashletReceivedCommandEvent(
    TotoWashletEntity, InfraredReceiverConsumerEntity, EventEntity
):
    """Event entity that fires when a TOTO Washlet IR command is received."""

    _attr_translation_key = "received_command"
    _attr_event_types = _EVENT_TYPES

    def __init__(self, entry: ConfigEntry, receiver_entity_id: str) -> None:
        """Initialize the event entity."""
        super().__init__(entry, unique_id_suffix="received_command")
        self._infrared_receiver_entity_id = receiver_entity_id

    @callback
    def _handle_signal(self, signal: InfraredReceivedSignal) -> None:
        """Handle a received IR signal."""
        command_code = TotoWashletCode.from_raw_timings(signal.timings)
        if command_code is None:
            event_type = _EVENT_TYPE_UNKNOWN
        else:
            event_type = _COMMAND_CODE_TO_EVENT_TYPE[command_code]

        _LOGGER.debug("Received TOTO Washlet IR command: %s", event_type)
        self._trigger_event(event_type)
        self.async_write_ha_state()
