import machine
import time
adc = machine.ADC(0)
pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
while True:
    vol_val = adc.read()
    pwm.duty(vol_val)
    print(vol_val)
    time.sleep(0.1)
    
