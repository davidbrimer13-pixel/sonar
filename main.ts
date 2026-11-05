// KY-050 / HC-SR04-style ultrasonic sensor
// Wiring: TRIG -> P0, ECHO -> P1, GND -> GND.
// IMPORTANT: If the sensor is powered at 5 V, connect ECHO to P1 through
// a voltage divider or logic-level shifter. Never feed 5 V directly to P1.

basic.forever(function () {
    let distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.Centimeters)

    if (distance > 0) {
        basic.showNumber(distance)
    } else {
        basic.showIcon(IconNames.No)
    }

    basic.pause(200)
})
