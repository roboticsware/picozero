from picozero import Stepper
from time import sleep

# Connect ULN2003 driver IN1-IN4 to Pico GP1, GP2, GP3, GP4
stepper = Stepper((1, 2, 3, 4))

# Rotate 1 full turn clockwise
stepper.rotate(1, "cw")
sleep(1)

# Rotate 1 full turn counter-clockwise
stepper.rotate(1, "ccw")
sleep(1)

# Rotate half turn (180 degrees)
stepper.turn(0.5, "cw")
sleep(1)

# Stop and release motor coils
stepper.stop()
