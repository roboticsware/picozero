from picozero import Motor
from time import sleep

motor = Motor(14, 15)

motor.forward()
sleep(1)
motor.stop()