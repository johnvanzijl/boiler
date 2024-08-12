import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

from .const import CONF_BOILER_ID, CONF_INVERT_X, CONF_INVERT_Y

DEPENDENCIES = ["uart"]
MULTI_CONF = True

boiler_ns = cg.esphome_ns.namespace("boiler")
BOILER = boiler_ns.class_("BOILER", cg.PollingComponent, uart.UARTDevice)

PresenceRegion = boiler_ns.class_("PresenceRegion")

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(BOILER),
    cv.Optional(CONF_INVERT_X, default=False): cv.boolean,
    cv.Optional(CONF_INVERT_Y, default=False): cv.boolean,
}).extend(cv.polling_component_schema("1s")).extend(uart.UART_DEVICE_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    if invert_x := config.get(CONF_INVERT_X):
        cg.add_define("INVERT_X")
    if invert_y := config.get(CONF_INVERT_Y):
        cg.add_define("INVERT_Y")
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)