import machine
import time 
#########lab1 question2 for iot#########
pin1 = machine.Pin(2, machine.Pin.OUT)
pin2 = machine.Pin(0, machine.Pin.OUT)

while True: 
    pin1.on()
    pin2.on()
    time.sleep_ms(500)
    pin1.off()
    time.sleep_ms(500)
    pin2.off()
    pin1.on()
    time.sleep_ms(500)
    pin1.off()
    time.sleep_ms(500)
    


