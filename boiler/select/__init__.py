import esphome.codegen as cg
from esphome.components import select
import esphome.config_validation as cv
from esphome.const import (
    ENTITY_CATEGORY_CONFIG,
    CONF_BAUD_RATE,
    ICON_THERMOMETER,
    ICON_NEW_BOX,
    CONF_INITIAL_VALUE,
    CONF_RESTORE_VALUE
)
from .. import BOILER, boiler_ns
from ..const import CONF_REGIONS_TYPE, CONF_BOILER_ID

BaudRateSelect = boiler_ns.class_("BaudRateSelect",
    select.Select,
    cg.Component,
    cg.Parented.template(BOILER)
)
RegionsType = boiler_ns.class_("RegionsType", select.Select, cg.Parented.template(BOILER))

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_BOILER_ID): cv.use_id(BOILER),
    cv.Optional(CONF_BAUD_RATE): select.select_schema(
        BaudRateSelect,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_THERMOMETER,
    ).extend({
        cv.Optional(CONF_INITIAL_VALUE, default="256000"): cv.string,
        cv.Optional(CONF_RESTORE_VALUE, default=True): cv.boolean,
    }),
    cv.Optional(CONF_REGIONS_TYPE): select.select_schema(
        RegionsType,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_NEW_BOX,
    )
}


async def to_code(config):
    boiler = await cg.get_variable(config[CONF_BOILER_ID])
    if baud_rate_config := config.get(CONF_BAUD_RATE):
        s = await select.new_select(
            baud_rate_config,
            options=[
                "9600",
                "19200",
                "38400",
                "57600",
                "115200",
                "230400",
                "256000",
                "460800",
            ],
        )

        await cg.register_component(s, baud_rate_config)
        cg.add(s.set_initial_value(baud_rate_config[CONF_INITIAL_VALUE]))
        cg.add(s.set_restore_value(baud_rate_config[CONF_RESTORE_VALUE]))

        hub = await cg.get_variable(config[CONF_BOILER_ID])
        cg.add(s.set_parent(hub))

    if regions_type_config := config.get(CONF_REGIONS_TYPE):
        s = await select.new_select(
            regions_type_config,
            options=[
                "Not used",
                "Detect",
                "Ignore",
            ],
        )

        await cg.register_parented(s, config[CONF_BOILER_ID])
        cg.add(boiler.set_regions_type_select(s))
