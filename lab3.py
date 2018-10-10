import machine
import ssd1306
import time

# mode 0: show current time
#mode 1: set clock
#mode 2: set alert change clk to alarm 
#mode 3: close alarm
########################################################################
'''def change_time(old,new):
    for k in range(0,len(old)):
        old[k] = int(old[k])
    for i in range(0,4):
        new[i] = old[i]
    if old[6] > 60:
        new[6] = old[6] - 60
        old[5] = old[5] + 1
    if old[5] > 60:
        new[5] = old[5] - 61
        old[4] = old[4] + 1
    if old[4] >24:
        new[4] = old[4] -25
    return new'''
    '''
    def action(i,temp):
    temp[i] = int(temp[i])+1
    old = temp
    new = old[:]
    time_format = change(old,new)
    date_on_screen, time_on_screen = format(time_format)
    return date_on_screen, time_on_screen
    '''
    #################################################################
    '''
    def callback_change(p):
    global date_on_screen
    global time_on_screen 
    if counter_second == 0:
        #change hour
        i = 4
        temp = rtc.datetime()
        date_on_screen, time_on_screen = action(i,temp)
    elif counter_second == 1:
        #change minute
        i = 5
        temp = rtc.datetime()
        date_on_screen, time_on_screen = action(i,temp)
    elif counter_second ==2:
        #change seconds
        i = 6
        temp = rtc.datetime()
        date_on_screen, time_on_screen = action(i,temp)
    '''
###########################callback test##################################
def callback_pointer(p):
    global state_second
    global counter_second
    a = p.value()
    time.sleep(0.1)
    a_after = p.value()
    if counter % 4 == 0:
        if (a==a_after):
            counter_second += 1
            if counter_second >=3:
                counter_second = 0
    '''if counter % 4 == 0:
                    #command
                if counter % 4 == 2:
                    #command
                if counter % 4 == 3:
                    #command'''
    print(counter_second)

def callback_change(p):
    global state_second
    global counter_second
    a = p.value()
    time.sleep(0.1)
    a_after = p.value()
    if counter % 4 == 0:
        if (a==a_after):
            state_second = - state_second
        if state_second == 1:
            counter_second += 1


def callback(p):
    global state
    global counter
    a = p.value()
    time.sleep(0.1)
    a_after = p.value()
    if (a==a_after):
        state = -state
    if state == 1:
        counter += 1
        print(counter)


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
#button_b press down is 0 and bounce up is 1
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

state = 1
counter = 0
state_second = 1
counter_second = 0
######################test case test the interruption########################
Button_C.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=callback)# can ignore theachine.Pin.IRQ_RISING,
##############################################

Button_A.irq(trigger= machine.Pin.IRQ_RISING, handler=callback_pointer)


while True:
    # Adjust brightness
    back_light = adc.read()
    oled.contrast(int(255*back_light /1023))
    # Get regular time format
    date_on_screen, time_on_screen = format(rtc.datetime())
    oled.fill(0)        # clear
    clk_state = date_on_screen
    oled.text('clk'+clk_state, 0, 0)
    oled.text(date_on_screen, 0, 10)
    oled.text(time_on_screen, 0, 20)
    oled.show()
