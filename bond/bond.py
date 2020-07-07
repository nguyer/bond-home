import requests
from bond.const import (Actions, DeviceTypes, Directions, Brightness)


class Bond:
    def __init__(self, bondIp, bondToken):
        self.bondIp = bondIp
        self.bondToken = bondToken

    def stop(self, deviceId):
        return self.doAction(deviceId, Actions.STOP)

    # Relating to Generic Device (GX)
    def turnOn(self, deviceId):
        return self.doAction(deviceId, Actions.TURN_ON)

    def turnOff(self, deviceId):
        return self.doAction(deviceId, Actions.TURN_OFF)

    def togglePower(self, deviceId):
        return self.doAction(deviceId, Actions.TOGGLE_POWER)

    # Relating to Motorized Shades (MS), Dimmers and Garage Doors
    def open(self, deviceId):
        return self.doAction(deviceId, Actions.OPEN)

    def toggleOpen(self, deviceId):
        return self.doAction(deviceId, Actions.TOGGLE_OPEN)

    def close(self, deviceId):
        return self.doAction(deviceId, Actions.CLOSE)

    def hold(self, deviceId):
        return self.doAction(deviceId, Actions.HOLD)

    def pair(self, deviceId):
        return self.doAction(deviceId, Actions.PAIR)

    def preset(self, deviceId):
        return self.doAction(deviceId, Actions.PRESET)

    # Relating to Ceiling Fan (CF)
    def setSpeed(self, deviceId, speed=3):
        return self.doAction(deviceId, 
                             Actions.SET_SPEED, 
                             {"argument": speed})

    def increaseSpeed(self, deviceId, speed=1):
        return self.doAction(deviceId, 
                             Actions.INCREASE_SPEED, 
                             {"argument": speed})

    def decreaseSpeed(self, deviceId, speed=1):
        return self.doAction(deviceId, 
                             Actions.DECREASE_SPEED, 
                             {"argument": speed})

    def setDirection(self, deviceId, direction=Directions.FORWARD):
        if direction != Directions.FORWARD and direction != Directions.REVERSE:
            raise InvalidDirectionException

        return self.doAction(deviceId, 
                             Actions.SET_DIRECTION, 
                             {"argument": direction})

    def toggleDirection(self, deviceId):
        return self.doAction(deviceId, Actions.TOGGLE_DIRECTION)

    def turnLightOn(self, deviceId):
        return self.doAction(deviceId, Actions.TURN_LIGHT_ON)

    def turnLightOff(self, deviceId):
        return self.doAction(deviceId, Actions.TURN_LIGHT_OFF)

    def toggleLight(self, deviceId):
        return self.doAction(deviceId, Actions.TOGGLE_LIGHT)

    def setBrightness(self, deviceId, brightness=Brightness.MIN):
        if brightness == 0:
            return self.doAction(deviceId, Actions.TURN_LIGHT_OFF)

        if brightness < Brightness.MIN or brightness > Brightness.MAX:
            raise InvalidBrightnessException

        return self.doAction(deviceId, 
                             Actions.SET_BRIGHTNESS, 
                             {"argument": brightness})

    # Relating to Fireplace (FP)
    def setFlame(self, deviceId, flame=3):
        return self.doAction(deviceId, 
                             Actions.SET_FLAME, 
                             {"argument": flame})

    def increaseFlame(self, deviceId, flame=1):
        return self.doAction(deviceId, 
                             Actions.INCREASE_FLAME, 
                             {"argument": flame})

    def decreaseFlame(self, deviceId, flame=1):
        return self.doAction(deviceId, 
                             Actions.DECREASE_FLAME, 
                             {"argument": flame})

    def doAction(self, deviceId, action, payload={}):
        url = f"http://{self.bondIp}/v2/devices/{deviceId}/actions/{action}"
        headers = {'BOND-Token': self.bondToken}

        r = requests.put(url, headers=headers, json=payload)
        if r.status_code < 200 or r.status_code > 299:
            raise Exception(r.content)
        return r.content

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


class InvalidBrightnessException(Exception):
    """Invalid brightness exception"""


class InvalidDirectionException(Exception):
    """Invalid direction exception"""
