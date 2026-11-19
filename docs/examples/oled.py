from picozero import OLED

oled = OLED(scl=3, sda=2)  # I2C1 (3.3V native, driver="ssd1306" or "sh1106")
oled.clear()
oled.text("Hello, picozero!", 0, 0)
oled.text("SSD1306 / SH1106", 0, 16)
oled.rect(0, 32, 128, 24)
oled.text("3.3V Safe I2C", 12, 40)
oled.show()
