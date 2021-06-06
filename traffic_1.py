from gpiozero import LED,TrafficLights,Button
from time import sleep

from gpiozero.exc import GPIOZeroError 

lights = TrafficLights(27,17,4)
lights_2=TrafficLights(16,20,21)
red_p1=LED(22)
green_p1=LED(5)
#traffic lights for pedestions 2
red_p2=LED(13)
green_p2=LED(6)
button_p1=Button(23)
button_p2=Button(24)
button=Button(18)

def turn_on():
    global lights,lights_2,button_p1,button_p2
    #while True:
    if   button_p2.is_pressed or   button_p1.is_pressed:
        lights.green.off()
        lights_2.green.off()
        lights.amber.on()
        lights_2.amber.on()
        sleep(1)
        lights.amber.off()
        lights_2.amber.off()
        lights.red.on()
        lights_2.red.on()
        red_p1.off()
        red_p2.off()
        green_p1.on()
        green_p2.on()
        lights.red.off()
        lights_2.red.off()

        sleep(3)
    elif button.is_pressed:
        exit()
           
    else:
        green_p1.off()
        green_p2.off()
        red_p1.on()
        red_p2.on()
        lights.green.on()  
        lights_2.green.on()
            #red_p1.on()
            #red_p2.on()
            
try:
    if __name__ == "__main__":
        while True:
            turn_on()
except KeyboardInterrupt:
    pass   