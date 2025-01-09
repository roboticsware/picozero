from picozero import I2cLcd
from time import sleep

lcd =  I2cLcd(19, 18)  # scl=19, sda=18

lcd.putstr('Hello World')
sleep(1)
lcd.move_to(0, 1)
lcd.putstr('Hello Pi Pico')