#include "reboot_button.h"

namespace esphome {
namespace boiler {

void RebootButton::press_action() { this->parent_->reboot_and_read(); }

}  // namespace boiler
}  // namespace esphome