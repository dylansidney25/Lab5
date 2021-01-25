from gpiozero import Button # import moduel LED
from gpiozero import LED # import moduel LED
from time import sleep
button = Button(2)
led = LED(17)

while True:
    if button.is_pressed:
        print("pressed")
        led.on() #set the gpio 17 to high
    else:
        print("Released")
    led.off() # set gpio 17 to low
    sleep(1)                   
