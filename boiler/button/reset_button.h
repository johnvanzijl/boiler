#pragma once

#include "esphome/components/button/button.h"
#include "../boiler.h"

namespace esphome {
namespace boiler {

class ResetButton : public button::Button, public Parented<BOILER> {
    public:
        ResetButton() = default;

    protected:
        void press_action() override;
};

}  // namespace boiler
}  // namespace esphome