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
            

