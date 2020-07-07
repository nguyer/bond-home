class Actions:
    # Note that Bond Action "Stop" instructs the Bond Bridge to stop sending.
    # There are other actions such as "Hold" that send a message to stop the
    # controlled-device's current action
    STOP = "Stop"

    # Relating to Generic Device (GX)
    TURN_ON = "TurnOn"
    TURN_OFF = "TurnOff"
    TOGGLE_POWER = "TogglePower"

    # Relating to Motorized Shades (MS), Dimmers and Garage Doors
    OPEN = "Open"
    TOGGLE_OPEN = "ToggleOpen"
    CLOSE = "Close"
    HOLD = "Hold"
    PAIR = "Pair"
    PRESET = "Preset"

    # Relating to Ceiling Fan (CF)
    SET_SPEED = "SetSpeed"
    INCREASE_SPEED = "IncreaseSpeed"
    DECREASE_SPEED = "DecreaseSpeed"

    TURN_LIGHT_ON = "TurnLightOn"
    TURN_LIGHT_OFF = "TurnLightOff"
    TOGGLE_LIGHT = "ToggleLight"

    SET_BRIGHTNESS = "SetBrightness"

    SET_DIRECTION = "SetDirection"
    TOGGLE_DIRECTION = "ToggleDirection"

    # Relating to Fireplace (FP)
    SET_FLAME = "SetFlame"
    INCREASE_FLAME = "IncreaseFlame"
    DECREASE_FLAME = "DecreaseFlame"


class DeviceTypes:
    CEILING_FAN = "CF"
    FIREPLACE = "FP"
    MOTORIZED_SHADES = "MS"
    GENERIC_DEVICE = "GX"


class Directions:
    FORWARD = 1
    REVERSE = -1


class Brightness:
    MIN = 1
    MAX = 100
