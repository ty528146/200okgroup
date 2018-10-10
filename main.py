import machine
import time 
#########lab1 question2 for iot#########
pin = machine.Pin(2, machine.Pin.OUT)
list1 =[0.2,1,0.2]
while True:
    for i in range(0,3):
        for j in range(0,3):
            pin.on()
            time.sleep(list1[i])
            pin.off()
            time.sleep(list1[i])
            
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
    
        


