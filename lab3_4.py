import machine
import ssd1306
import time
from datetime import tzinfo, timedelta, datetime



class FixedOffset(tzinfo):

    def __init__(self, offset):

        self.__offset = timedelta(hours=offset)

        self.__dst = timedelta(hours=offset-1)

        self.__name = ''


    def utcoffset(self, dt):

        return self.__offset


    def tzname(self, dt):

        return self.__name


    def dst(self, dt):

        return self.__dst



now_time = datetime.now()

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

oled.fill(0)
oled.pixel(12, 2, 1)
oled.show()
oled.fill(0)

oled.text('clk', 0, 0)
oled.text('16:51:42', 0, 10)
oled.show()
sleep(1)
oled.fill(1)
oled.contrast(64)
oled.show()
sleep(1)
oled.contrast(200)
oled.show()
sleep(1)
oled.fill(0)
oled.show()


while True:
    time.sleep(1)
    oled.fill(0)
    oled.text('clk', 0, 0)
    oled.text('16:51:43', 0, 10)
    oled.show()
