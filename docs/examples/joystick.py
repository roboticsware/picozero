from picozero import Pot, Button
from time import sleep

x = Pot(27)
y = Pot(26)
button = Button(17)

while True:
    if button.is_pressed:
        print("Button is pressed\n")

    print("x: " + str(x.raw_value) + ", y: " + str(y.raw_value))
    sleep(0.1)