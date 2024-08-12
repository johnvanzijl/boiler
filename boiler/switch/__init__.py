import esphome.codegen as cg
from esphome.components import switch
import esphome.config_validation as cv
from esphome.const import (
    DEVICE_CLASS_SWITCH,
    ICON_BLUETOOTH,
    ENTITY_CATEGORY_CONFIG,
    ICON_PULSE,
    CONF_INITIAL_VALUE,
    CONF_RESTORE_VALUE
)
from .. import BOILER, boiler_ns
from ..const import CONF_SINGLE_TARGET, CONF_BLUETOOTH, CONF_BOILER_ID

BluetoothSwitch = boiler_ns.class_("BluetoothSwitch",
    switch.Switch,
    cg.Component,
    cg.Parented.template(BOILER)
)
SingleTargetSwitch = boiler_ns.class_("SingleTargetSwitch",
    switch.Switch,
    cg.Parented.template(BOILER)
)

CONFIG_SCHEMA = {
    cv.GenerateID(CONF_BOILER_ID): cv.use_id(BOILER),
    cv.Optional(CONF_SINGLE_TARGET): switch.switch_schema(
        SingleTargetSwitch,
        device_class=DEVICE_CLASS_SWITCH,
        entity_category=ENTITY_CATEGORY_CONFIG,
        icon=ICON_PULSE,
    ),
}


async def to_code(config):
    boiler = await cg.get_variable(config[CONF_BOILER_ID])
    if single_target_config := config.get(CONF_SINGLE_TARGET):
        s = await switch.new_switch(single_target_config)
        await cg.register_parented(s, config[CONF_BOILER_ID])
        cg.add(boiler.set_single_target_switch(s))
    if bluetooth_config := config.get(CONF_BLUETOOTH):
        s = await switch.new_switch(bluetooth_config)
        await cg.register_component(s, bluetooth_config)
        cg.add(s.set_initial_value(bluetooth_config[CONF_INITIAL_VALUE]))
        cg.add(s.set_restore_value(bluetooth_config[CONF_RESTORE_VALUE]))

        hub = await cg.get_variable(config[CONF_BOILER_ID])
        cg.add(s.set_parent(hub))
