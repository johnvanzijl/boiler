#include "reset_button.h"

namespace esphome {
namespace boiler {

void ResetButton::press_action() { this->parent_->restore_factory(); }

}  // namespace boiler
}  // namespace esphome