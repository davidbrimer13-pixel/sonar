"""Read a KY-050 / HC-SR04-style ultrasonic sensor with a micro:bit.

Wiring (use a common ground):
  Sensor VCC  -> suitable 5 V supply (check your module's requirements)
  Sensor GND  -> micro:bit GND and supply GND
  Sensor TRIG -> micro:bit P0
  Sensor ECHO -> micro:bit P1 through a voltage divider / level shifter

Do not connect a 5 V ECHO signal directly to a micro:bit pin. For example,
a 1 kΩ resistor from ECHO to P1 and a 2 kΩ resistor from P1 to GND makes
a divider that reduces about 5 V to about 3.3 V.
"""

from microbit import *

TRIG = pin0
ECHO = pin1
ECHO_TIMEOUT_US = 30000  # Roughly 5 m maximum; also prevents waiting forever.


def distance_cm():
    """Return the measured distance in cm, or None if no echo is received."""
    TRIG.write_digital(0)
    sleep(2)
    TRIG.write_digital(1)
    # micro:bit sleep() has millisecond resolution; 1 ms exceeds the sensor's
    # minimum trigger pulse, which is typically around 10 microseconds.
    sleep(1)
    TRIG.write_digital(0)

    # get_pulse_us measures the HIGH pulse in microseconds. The echo must be
    # level-shifted before reaching P1 if the sensor is powered at 5 V.
    pulse_us = ECHO.get_pulse_us(1, timeout=ECHO_TIMEOUT_US)
    if pulse_us < 0:
        return None

    # Sound travels to the target and back; HC-SR04-style sensors use about
    # 58 microseconds per centimeter for the round trip.
    return pulse_us / 58.0


while True:
    distance = distance_cm()

    if distance is None:
        display.show(Image.NO)
        print("No echo")
    else:
        print("{:.1f} cm".format(distance))
        if distance < 10:
            display.show(Image.SAD)
        else:
            display.show(Image.HAPPY)

    sleep(200)
