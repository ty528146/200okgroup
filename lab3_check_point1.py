import machine
import ssd1306
import time
###########################callback test##################################
def callback(p):
    global state
    a = p.value()
    time.sleep(0.1)
    a_after = p.value()
    if (a==a_after):
        state = p.value()
        print(state)

def format(time_format):
    date_yyyy = str(time_format[0])
    date_mm = str(time_format[1])
    date_dd = str(time_format[2])
    time_hour = str(time_format[4])
    if int(time_hour)<10:
        time_hour = "0"+time_hour
    time_min = str(time_format[5])
    if int(time_min)<10:
        time_min = "0"+time_min
    time_sec = str(time_format[6])
    if int(time_sec)<10:
        time_sec = "0"+time_sec

    date_on_screen = date_yyyy + "/" + date_mm + "/" + date_dd
    time_on_screen = time_hour + ":" + time_min + ":" + time_sec
    return date_on_screen, time_on_screen

###########################callback test##################################


# i2c & OLED
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
# RTC
rtc = machine.RTC()
rtc.datetime((2014, 5, 1, 4, 13, 9, 40, 0))
# ADC
adc = machine.ADC(0)
# PWM/BLINK
pwm15 = machine.PWM(machine.Pin(15), freq=1)  
pwm15.duty(512)  # create and configure in one go
# Button
Button_A = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
Button_B = machine.Pin(16, machine.Pin.IN)        # Button B has a 100K pullup
Button_C = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
# # # # # # # # # # # # # # # # # # # # # # 
##########test case initital state#############
oled.fill(0)
oled.pixel(12, 2, 1)
oled.show()
time.sleep(1)

oled.fill(1)
oled.pixel(12, 2, 0)
oled.show()
time.sleep(1)

oled.fill(0)
oled.show()
time.sleep(1)

state = 0
######################test case test the interruption########################
Button_C.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=callback)
##############################################

while True:
    # Adjust brightness
    back_light = adc.read()
    oled.contrast(int(255*back_light /1023))
    # Get regular time format
    date_on_screen, time_on_screen = format(rtc.datetime())
    oled.fill(0)        # clear
    oled.text('clk', 0, 0)
    oled.text(date_on_screen, 0, 10)
    oled.text(time_on_screen, 0, 20)
    oled.show()
