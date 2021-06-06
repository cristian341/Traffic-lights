from gpiozero import LED,TrafficLights,Button
from time import sleep 

lights = TrafficLights(27,17,4)
lights_2=TrafficLights(16,20,21)
red_p1=LED(22)
green_p1=LED(5)
#traffic lights for pedestions 2
red_p2=LED(13)
green_p2=LED(6)
button=Button(18)

def turn_on():
    global lights,lights_2,red_p1,red_p2,green_p1,green_p2,button
    while True:
        if button.is_pressed:
            exit()
        else:
            red_p1.on()
            red_p2.on()
            lights.green.on()  
            lights_2.green.on()
            sleep(3)
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
            sleep(3)
            green_p1.off()
            green_p2.off()
            lights.amber.on()
            lights_2.amber.on()
            sleep(1)
            lights.red.off()
            lights_2.red.off()
            lights.amber.off()
            lights_2.amber.off()
    




try:
    if __name__ == "__main__":
        while True:
            turn_on()

except KeyboardInterrupt:
    pass

