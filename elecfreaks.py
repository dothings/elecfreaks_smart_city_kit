import time
import machine

from microbit import *

class SonarBit:
    """
        class to get distance measurements from
        the elecfreaks 1-wire sonar:bit as found
        in the smart city kit
    """

    def __init__(self, pin):
        # pins = [pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9]
        self.pin = pin

    def distance(self):
        """ Activate the sensor and measure distance in cm """

        # activate the sensor with a 10 us pulse (1-wire)
        self.pin.write_digital(0)
        time.sleep_us(2)
        self.pin.write_digital(1)
        time.sleep_us(10)
        self.pin.write_digital(0)

        # measure duration of the echo pulse, timeout set on 30ms
        # since it can only measure so far (guessing approx 3 meters)
        duration = machine.time_pulse_us(self.pin, 1, 30000)

        if duration < 0:
            return None  # time out caught

        # calculate distance based on return time
        # and speed of sound (343m/s = 0.0343 cm/us)
        distance_in_cm = (duration / 2) * 0.0343

        return distance_in_cm


class Led:
    """
        simple implementation of led
        for turning a led on and off
    """

    def __init__(self, pin):
        self.pin = pin
        self.state = False

    def on(self):
        self.pin.write_digital(1)
        self.state = True

    def off(self):
        self.pin.write_digital(0)
        self.state = False

    def flip(self):
        # change on to off and off to on
        if self.state:
            self.off()
        else:
            self.on()

class SoilMoistureSensor:
    """ soil moisture sensor (two pins)

    takes: pin
    returns: int 0-100 (%)
    """
    def __init__(self, pin):
        self.pin = pin

    def measure(self):
        reading = self.pin.read_analog()
        value = (reading * 100) / 1023
        return value


class WaterLevelSensor:
    """ water level sensor (rectangle)

    this sensor is wierd, not found a logical
    reading to % calculation

    takes: pin
    returns: int 0-100 (%)
    """
    def __init__(self, pin):
        self.pin = pin

    def measure(self):
        reading = self.pin.read_analog()
        value = 0
        if reading > 300:
            value = (reading -300) / 2
        return value


