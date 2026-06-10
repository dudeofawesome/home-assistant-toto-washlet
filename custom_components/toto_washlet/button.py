"""Button platform for the TOTO Washlet integration."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.components.infrared import InfraredEmitterConsumerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from .commands import TotoWashletCode
from .const import CONF_INFRARED_ENTITY_ID
from .entity import TotoWashletEntity

PARALLEL_UPDATES = 1


@dataclass(frozen=True, kw_only=True)
class TotoWashletButtonEntityDescription(ButtonEntityDescription):
    """Describes TOTO Washlet button entity."""

    command_code: TotoWashletCode


BUTTON_DESCRIPTIONS: tuple[TotoWashletButtonEntityDescription, ...] = (
    TotoWashletButtonEntityDescription(
        key="stop",
        translation_key="stop",
        icon="mdi:stop",
        command_code=TotoWashletCode.STOP,
    ),
    TotoWashletButtonEntityDescription(
        key="rear",
        translation_key="rear",
        icon="mdi:shower-head",
        command_code=TotoWashletCode.REAR,
    ),
    TotoWashletButtonEntityDescription(
        key="soft_rear",
        translation_key="soft_rear",
        icon="mdi:water-opacity",
        command_code=TotoWashletCode.SOFT_REAR,
    ),
    TotoWashletButtonEntityDescription(
        key="front",
        translation_key="front",
        icon="mdi:spray",
        command_code=TotoWashletCode.FRONT,
    ),
    TotoWashletButtonEntityDescription(
        key="oscillate",
        translation_key="oscillate",
        icon="mdi:arrow-oscillating",
        command_code=TotoWashletCode.OSCILLATE,
    ),
    TotoWashletButtonEntityDescription(
        key="pulsate",
        translation_key="pulsate",
        icon="mdi:pulse",
        command_code=TotoWashletCode.PULSATE,
    ),
    TotoWashletButtonEntityDescription(
        key="dryer",
        translation_key="dryer",
        icon="mdi:fan",
        command_code=TotoWashletCode.DRYER,
    ),
    TotoWashletButtonEntityDescription(
        key="power_deodorizer",
        translation_key="power_deodorizer",
        icon="mdi:air-filter",
        command_code=TotoWashletCode.POWER_DEODORIZER,
    ),
    TotoWashletButtonEntityDescription(
        key="user_1",
        translation_key="user_1",
        icon="mdi:account",
        command_code=TotoWashletCode.USER_1,
    ),
    TotoWashletButtonEntityDescription(
        key="user_2",
        translation_key="user_2",
        icon="mdi:account",
        command_code=TotoWashletCode.USER_2,
    ),
    TotoWashletButtonEntityDescription(
        key="lid_open_close",
        translation_key="lid_open_close",
        icon="mdi:toilet",
        command_code=TotoWashletCode.LID_OPEN_CLOSE,
    ),
    TotoWashletButtonEntityDescription(
        key="seat_open_close",
        translation_key="seat_open_close",
        icon="mdi:seat",
        command_code=TotoWashletCode.SEAT_OPEN_CLOSE,
    ),
    TotoWashletButtonEntityDescription(
        key="full_flush",
        translation_key="full_flush",
        icon="mdi:water-pump",
        command_code=TotoWashletCode.FULL_FLUSH,
    ),
    TotoWashletButtonEntityDescription(
        key="light_flush",
        translation_key="light_flush",
        icon="mdi:water",
        command_code=TotoWashletCode.LIGHT_FLUSH,
    ),
    TotoWashletButtonEntityDescription(
        key="eco_flush",
        translation_key="eco_flush",
        icon="mdi:leaf",
        command_code=TotoWashletCode.ECO_FLUSH,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up TOTO Washlet buttons from config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_ENTITY_ID]
    async_add_entities(
        TotoWashletButton(entry, infrared_entity_id, description)
        for description in BUTTON_DESCRIPTIONS
    )


class TotoWashletButton(
    TotoWashletEntity, InfraredEmitterConsumerEntity, ButtonEntity
):
    """TOTO Washlet button entity."""

    entity_description: TotoWashletButtonEntityDescription

    def __init__(
        self,
        entry: ConfigEntry,
        infrared_entity_id: str,
        description: TotoWashletButtonEntityDescription,
    ) -> None:
        """Initialize TOTO Washlet button."""
        super().__init__(entry, unique_id_suffix=description.key)
        self._infrared_emitter_entity_id = infrared_entity_id
        self.entity_description = description

    async def async_press(self) -> None:
        """Press the button."""
        await self._send_command(self.entity_description.command_code.to_command())
