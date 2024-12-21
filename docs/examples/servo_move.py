from picozero import Servo
from time import sleep

# Check the specifications SG-90 model
# Pulse width: 500 ~ 2400 µs
servo = Servo(1, 0, 0.5 / 1000, 2.4 /1000)

servo.move_to_degree(0)
sleep(1)

servo.move_to_degree(90)
sleep(1)

servo.move_to_degree(180)
sleep(1)

servo.off()