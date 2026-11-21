from picozero import Servo
from time import sleep

# Use a 3.3V-compatible micro servo (e.g. FS90, 3V-6V wide-voltage micro servo)
# Pulse width: adjust to your servo model (commonly 500 ~ 2400 µs, or standard 1000 ~ 2000 µs)
servo = Servo(1, min_pulse_width=0.5 / 1000, max_pulse_width=2.4 / 1000)

servo.move_to_degree(0)
sleep(1)

servo.move_to_degree(90)
sleep(1)

servo.move_to_degree(180)
sleep(1)

servo.off()
