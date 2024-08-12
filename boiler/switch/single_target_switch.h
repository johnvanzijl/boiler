#pragma once

#include "esphome/components/switch/switch.h"
#include "../boiler.h"

namespace esphome {
namespace boiler {

class SingleTargetSwitch : public switch_::Switch, public Parented<BOILER> {
    public:
        SingleTargetSwitch() = default;

    protected:
        void write_state(bool state) override;
};

}  // namespace boiler
}  // namespace esphome