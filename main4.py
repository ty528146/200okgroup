import time
import machine
pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
pwm.duty(1023)
pwm.duty(512)
pwm.duty(0)
