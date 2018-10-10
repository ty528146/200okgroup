import time
import machine
pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
while True:
    for i in range(1024):
        pwm.duty(i)
        time.sleep(0.01)
        #0.01 more flat
    for i in range(1023, -1, -1):
        pwm.duty(i)
        time.sleep(0.001)
        #dim very fast 0.001 faster
