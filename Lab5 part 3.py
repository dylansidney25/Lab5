from gpiozero import PWMLED
from time import sleep
import math

led = PWMLED(17)
n = 0
x = 0
brightness = 0
position = 0
brightness_levels = 10
time_on = 3.3

while x < 10:
    while n <= brightness_levels:
        position = (n/brightness_levels) * (math.pi) #finds ratio of pi for how many levels there are. this will give a value on the range of 0 to pi as 0 * pi = 0 and 1 * pi = pi
        brightness = math.sin(position) #finds the sin of the position, this will give a value from 0 to 1 then back to 0 as sin(0) = 0, sin(pi/2) = 1, and sin(pi) = 0
        led.value = brightness # sets the led brightness
        sleep(time_on/brightness_levels) #holds the brightness for a portion of time depening on desired time on and brightness levels
        n+=1
    n = 0
    x += 1



