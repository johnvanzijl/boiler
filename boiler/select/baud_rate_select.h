#pragma once

#include "esphome/components/select/select.h"
#include "esphome/core/preferences.h"
#include "../boiler.h"

namespace esphome {
namespace boiler {

class BaudRateSelect : public select::Select, public Component, public Parented<BOILER> {
    public:
        void setup() override;
        void set_initial_value(std::string initial_value) { this->initial_value_ = initial_value; }
        void set_restore_value(bool restore_value) { this->restore_value_ = restore_value; }

    protected:
        std::string initial_value_;
        bool restore_value_{true};
        ESPPreferenceObject pref_;
        void control(const std::string &value) override;
};

}  // namespace boiler
}  // namespace esphome