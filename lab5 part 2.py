from gpiozero import PWMLED
from time import sleep

led = PWMLED(17)

while True:
    led.value = 0 #off
    sleep(1)
    led.value = 0.25 #1/4
    sleep(1)
    led.value = 1 #full
    sleep(1)
    #i had to reduce the middle state to show a larger difference for video reasons
