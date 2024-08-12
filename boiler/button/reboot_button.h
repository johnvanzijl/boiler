#pragma once

#include "esphome/components/button/button.h"
#include "../boiler.h"

namespace esphome {
namespace boiler {

class RebootButton : public button::Button, public Parented<BOILER> {
    public:
        RebootButton() = default;

    protected:
        void press_action() override;
};

}  // namespace boiler
}  // namespace esphome