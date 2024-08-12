import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import number
from esphome.const import (
    DEVICE_CLASS_EMPTY,
    UNIT_DEGREES,
    ICON_ROTATE_RIGHT,
    ENTITY_CATEGORY_CONFIG,
    CONF_INITIAL_VALUE,
    CONF_RESTORE_VALUE,
    CONF_MIN_VALUE,
    CONF_MAX_VALUE,
    CONF_STEP,
    CONF_ENTITY_CATEGORY,
    DEVICE_CLASS_DISTANCE,
    CONF_ID,
    ICON_ACCELERATION_X,
    ICON_ACCELERATION_Y,
    UNIT_CENTIMETER,
    UNIT_SECOND,
    CONF_UNIT_OF_MEASUREMENT
)
from .. import BOILER, boiler_ns, PresenceRegion

from ..const import (CONF_PRESENCE_TIMEOUT, CONF_X0, CONF_Y0, CONF_X1, CONF_Y1, CONF_X, CONF_Y,
    CONF_BOILER_ID)

NUMBERS = [CONF_X0, CONF_Y0, CONF_X1, CONF_Y1]

DEPENDENCIES = ["boiler"]


PresenceTimeoutNumber = boiler_ns.class_(
    "PresenceTimeoutNumber",
    number.Number,
    cg.Component,
    cg.Parented.template(BOILER)
)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_BOILER_ID): cv.use_id(BOILER),
    cv.Optional(CONF_PRESENCE_TIMEOUT): number.NUMBER_SCHEMA.extend(
        {
            cv.GenerateID(): cv.declare_id(PresenceTimeoutNumber),
            cv.Optional(
                CONF_ENTITY_CATEGORY, default=ENTITY_CATEGORY_CONFIG
            ): cv.entity_category,
            cv.Optional(CONF_INITIAL_VALUE, default=0): cv.positive_float,
            cv.Optional(CONF_MAX_VALUE, default=6000): cv.positive_float,
            cv.Optional(CONF_MIN_VALUE, default=0): cv.positive_float,
            cv.Optional(CONF_RESTORE_VALUE, default=True): cv.boolean,
            cv.Optional(CONF_STEP, default=0.1): cv.positive_float,
            cv.Optional(CONF_UNIT_OF_MEASUREMENT, default=UNIT_SECOND): cv.string_strict
        }
    ).extend(cv.COMPONENT_SCHEMA),
})


async def to_code(config):
    boiler = await cg.get_variable(config[CONF_BOILER_ID])
    
    if presence_timeout_config := config.get(CONF_PRESENCE_TIMEOUT):
        var = await number.new_number(
            presence_timeout_config,
            min_value=presence_timeout_config[CONF_MIN_VALUE],
            max_value=presence_timeout_config[CONF_MAX_VALUE],
            step=presence_timeout_config[CONF_STEP],
        )
        await cg.register_component(var, presence_timeout_config)
        cg.add(var.set_initial_value(presence_timeout_config[CONF_INITIAL_VALUE]))
        cg.add(var.set_restore_value(presence_timeout_config[CONF_RESTORE_VALUE]))

        hub = await cg.get_variable(config[CONF_BOILER_ID])
        func = getattr(hub, f"set_presence_timeout_number")
        cg.add(func(var))
        cg.add(var.set_parent(hub))

