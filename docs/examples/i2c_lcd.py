from picozero import I2cLcd
from time import sleep

lcd =  I2cLcd(3, 2)  # scl=3, sda=2

lcd.putstr('Hello World')
sleep(1)
lcd.move_to(0, 1)
lcd.putstr('Hello Pi Pico')