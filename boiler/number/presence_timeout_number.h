#pragma once

#include "esphome/components/number/number.h"
#include "esphome/core/preferences.h"
#include "../boiler.h"

namespace esphome {
namespace boiler {

class PresenceTimeoutNumber : public number::Number, public Component, public Parented<BOILER>{
    public:
        void setup() override;
        void set_initial_value(float initial_value) { this->initial_value_ = initial_value; }
        void set_restore_value(bool restore_value) { this->restore_value_ = restore_value; }

    protected:
        float initial_value_{NAN};
        bool restore_value_{true};
        ESPPreferenceObject pref_;
        void control(float value) override;
};

}  // namespace boiler
}  // namespace esphome
