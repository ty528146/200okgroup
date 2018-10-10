import machine
import ssd1306
import time

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.pixel(12, 2, 1)
oled.show()

oled.text('clk', 0, 0)
oled.text('16:51:42', 0, 10)
oled.show()
time.sleep(1)
oled.text('16:51:43', 0, 10)
oled.show()
