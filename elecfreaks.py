import time
import machine

from microbit import *

class SonarBit:
    """
        class to get distance measurements from
        the elecfreaks 1-wire sonar:bit as found
        in the smart city kit

        takes pin on which the Sonarbit is connected
    """

    def __init__(self, pin):
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

    def on(self):
        self.pin.write_digital(1)

    def off(self):
        self.pin.write_digital(0)
