from machine import Pin
import time
import machine

def callbackup(p):
    time.sleep_ms(100)
    flag = p.value()
    if flag == 1:
       state = 1
    else:
        state = 0
    return state

def callbackdown(p):
    time.sleep_ms(100)
    flag = p.value()
    if flag == 0:
        state = 0
    else:
        state = 1
    return state       
 

adc = machine.ADC(0)
pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
button = Pin(16,PIN.in)
state = button.irq(trigger=Pin.IRQ_FALLING, handler=callbackup)
state = button.irq(trigger=Pin.IRQ_FALLING, handler=callbackdown)
while True:
    state = 
    vol_val = adc.read()
    if state == 1:
        pwm.duty(vol_val)
