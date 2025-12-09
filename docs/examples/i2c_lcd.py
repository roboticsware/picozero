from picozero import I2cLcd
from time import sleep

lcd =  I2cLcd(1, 27, 26)  # i2c_id=1, scl=27, sda=26

lcd.putstr('Hello World')
sleep(1)
lcd.move_to(0, 1)
lcd.putstr('Hello Pi Pico')