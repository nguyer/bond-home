import requests

BOND_DEVICE_TYPE_CEILING_FAN = "CF"
BOND_DEVICE_TYPE_FIREPLACE = "FP"
BOND_DEVICE_TYPE_MOTORIZED_SHADES = "MS"
BOND_DEVICE_TYPE_GENERIC_DEVICE = "GX"

# Note that Bond Action "Stop" instructs the Bond Bridge to stop sending.
# There are other actions such as "Hold" that send a message to stop the
# controlled-device's current action
BOND_DEVICE_ACTION_STOP = "Stop"

# Relating to Generic Device (GX)
BOND_DEVICE_ACTION_TURN_ON = "TurnOn"
BOND_DEVICE_ACTION_TURN_OFF = "TurnOff"
BOND_DEVICE_ACTION_TOGGLE_POWER = "TogglePower"

# Relating to Motorized Shades (MS), Dimmers and Garage Doors
BOND_DEVICE_ACTION_OPEN = "Open"
BOND_DEVICE_ACTION_TOGGLE_OPEN = "ToggleOpen"
BOND_DEVICE_ACTION_CLOSE = "Close"
BOND_DEVICE_ACTION_HOLD = "Hold"
BOND_DEVICE_ACTION_PAIR = "Pair"
BOND_DEVICE_ACTION_PRESET = "Preset"

# Relating to Ceiling Fan (CF)
BOND_DEVICE_ACTION_SET_SPEED = "SetSpeed"
BOND_DEVICE_ACTION_INCREASE_SPEED = "IncreaseSpeed"
BOND_DEVICE_ACTION_DECREASE_SPEED = "DecreaseSpeed"

BOND_DEVICE_ACTION_TURN_LIGHT_ON = "TurnLightOn"
BOND_DEVICE_ACTION_TURN_LIGHT_OFF = "TurnLightOff"
BOND_DEVICE_ACTION_TOGGLE_LIGHT = "ToggleLight"

# Relating to Fireplace (FP)
BOND_DEVICE_ACTION_SET_FLAME = "SetFlame"
BOND_DEVICE_ACTION_INCREASE_FLAME = "IncreaseFlame"
BOND_DEVICE_ACTION_DECREASE_FLAME = "DecreaseFlame"


class Bond:
    def __init__(self, bondIp, bondToken):
        self.bondIp = bondIp
        self.bondToken = bondToken

    def stop(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_STOP)

    # Relating to Generic Device (GX)
    def turnOn(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_TURN_ON)

    def turnOff(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_TURN_OFF)

    def togglePower(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_TOGGLE_POWER)

    # Relating to Motorized Shades (MS), Dimmers and Garage Doors
    def open(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_OPEN)

    def toggleOpen(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_TOGGLE_OPEN)

    def close(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_CLOSE)

    def hold(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_HOLD)

    def pair(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_PAIR)

    def preset(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_PRESET)

    # Relating to Ceiling Fan (CF)
    def setSpeed(self, deviceId, speed=3):
        return self.doAction(deviceId,
                             BOND_DEVICE_ACTION_SET_SPEED,
                             {"argument": speed})

    def increaseSpeed(self, deviceId, speed=1):
        return self.doAction(deviceId,
                             BOND_DEVICE_ACTION_INCREASE_SPEED,
                             {"argument": speed})

    def decreaseSpeed(self, deviceId, speed=1):
        return self.doAction(deviceId,
                             BOND_DEVICE_ACTION_DECREASE_SPEED,
                             {"argument": speed})

    def turnLightOn(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_TURN_LIGHT_ON)

    def turnLightOff(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_TURN_LIGHT_OFF)

    def toggleLight(self, deviceId):
        return self.doAction(deviceId, BOND_DEVICE_ACTION_TOGGLE_LIGHT)

    # Relating to Fireplace (FP)
    def setFlame(self, deviceId, flame=3):
        return self.doAction(deviceId,
                             BOND_DEVICE_ACTION_SET_FLAME,
                             {"argument": flame})

    def increaseFlame(self, deviceId, flame=1):
        return self.doAction(deviceId,
                             BOND_DEVICE_ACTION_INCREASE_FLAME,
                             {"argument": flame})

    def decreaseFlame(self, deviceId, flame=1):
        return self.doAction(deviceId,
                             BOND_DEVICE_ACTION_DECREASE_FLAME,
                             {"argument": flame})

    def doAction(self, deviceId, action, payload={}):
        url = f"http://{self.bondIp}/v2/devices/{deviceId}/actions/{action}"
        headers = {'BOND-Token': self.bondToken}

        r = requests.put(url, headers=headers, json=payload)
        if r.status_code < 200 or r.status_code > 299:
            raise Exception(r.content)
        return r.content

    def getVersion(self):
        url = f"http://{self.bondIp}/v2/sys/version"
        headers = {'BOND-Token': self.bondToken}

        r = requests.get(url, headers=headers)
        return r.json()

    def getDeviceIds(self):
        url = f"http://{self.bondIp}/v2/devices"
        headers = {'BOND-Token': self.bondToken}

        r = requests.get(url, headers=headers)
        devices = []
        for key in r.json():
            if (key != '_'):
                devices.append(key)
        return devices

    def getDevice(self, deviceId):
        url = f"http://{self.bondIp}/v2/devices/{deviceId}"
        headers = {'BOND-Token': self.bondToken}

        r = requests.get(url, headers=headers)
        return r.json()

    def getProperties(self, deviceId):
        url = f"http://{self.bondIp}/v2/devices/{deviceId}/properties/"
        headers = {'BOND-Token': self.bondToken}

        r = requests.get(url, headers=headers)
        return r.json()

    def getDeviceState(self, deviceId):
        url = f"http://{self.bondIp}/v2/devices/{deviceId}/state"
        headers = {'BOND-Token': self.bondToken}

        r = requests.get(url, headers=headers)
        return r.json()
