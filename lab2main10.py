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
    print(adc.read())
    time.sleep(0.1)
    print(adc.read())
    print(p.value())


def callback(p):
    print("hahahah i am callbackdown")
    print(adc.read())
    time.sleep(0.1)
    print(adc.read())
    print(p.value())
    voltage = p.value()
    if voltage ==0:
        while True:
            vol_val = adc.read()
            pwm.duty(vol_val)
    else:
        pwm.duty(10)
        sleep(3)

adc = machine.ADC(0)
pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
pwm.duty(1000)
time.sleep(2)
button = machine.Pin(2,machine.Pin.IN)

#button.irq(trigger=machine.Pin.IRQ_RISING, handler=callbackup)
button.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=callback)

pwm.duty(10)