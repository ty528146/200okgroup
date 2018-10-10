# from machine import Pin
import time
import machine

def callbackup(p):
    time.sleep_ms(100)
    flag = p.value()
    while True:
        vol_val = adc.read()
        pwm.duty(vol_val)
            
def callbackdown(p):
    time.sleep_ms(100)
    flag = p.value()
    while( flag == 0):
        vol_val = 500
        pwm.duty(vol_val)
      
          
 

adc = machine.ADC(0)
pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
pwm.duty(1000)
time.sleep(2)
#button = machine.Pin(16,machine.PIN.in)
#button.irq(trigger=machine.Pin.IRQ_RISING, handler=callbackup)
#button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callbackdown)
#pwm.duty(500)
