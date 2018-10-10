# from machine import Pin
import time
import machine

def callbackup(p):
    '''time.sleep_ms(300)
                flag = p.value()
                while True:
                    vol_val = adc.read()
                    pwm.duty(vol_val)'''
    
    #flag = p.value()
    global state
    print(adc.read())
    time.sleep(0.1)
    print(adc.read())
    print(p.value())


def callback(p):
    global state
    a = p.value()
    time.sleep(0.1)
    a_after = p.value()
    if (a==a_after):
        state = p.value()
    

adc = machine.ADC(0)
pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
pwm.duty(1000)
time.sleep(2)
button = machine.Pin(2,machine.Pin.IN)
state = 1
#button.irq(trigger=machine.Pin.IRQ_RISING, handler=callbackup)
button.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=callback)



while True:
    if state == 0:#gpio 初始化必须是下降沿
        pwm.duty(adc.read())
    else:
        pwm.duty(100)

