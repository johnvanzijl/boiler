import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv
from esphome.const import (
    ENTITY_CATEGORY_DIAGNOSTIC,
    CONF_VERSION,
    CONF_MAC_ADDRESS,
    ICON_BLUETOOTH,
    ICON_CHIP,
)
from . import BOILER
from .const import CONF_BOILER_ID

DEPENDENCIES = ["boiler"]

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_BOILER_ID): cv.use_id(BOILER),
    cv.Optional(CONF_VERSION): text_sensor.text_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC, icon=ICON_CHIP
    ),
    cv.Optional(CONF_MAC_ADDRESS): text_sensor.text_sensor_schema(
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC, icon=ICON_BLUETOOTH
    ),
}

async def to_code(config):
    boiler = await cg.get_variable(config[CONF_BOILER_ID])
    if version_config := config.get(CONF_VERSION):
        sens = await text_sensor.new_text_sensor(version_config)
        cg.add(boiler.set_version_text_sensor(sens))
    if mac_address_config := config.get(CONF_MAC_ADDRESS):
        sens = await text_sensor.new_text_sensor(mac_address_config)
        cg.add(boiler.set_mac_text_sensor(sens))
