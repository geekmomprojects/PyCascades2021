# CircuitPython LED Animation Demo base code for PyCascades 2021
import board
import random
# Uncomment your LED type
import neopixel
#import adafruit_dotstar

# Animation modules
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.color import colorwheel
from adafruit_led_animation.sequence import AnimationSequence

# Not enough memory for these on Gemma M0, Trinket M0, QTPy
#from adafruit_led_animation.animation.pulse import Pulse
#from adafruit_led_animation.animation.chase import Chase
#from adafruit_led_animation.animation.rainbow import Rainbow

##########################################
# SET THESE VALUES FOR YOUR BOARD and LEDS
data_pin = board.D1
#clock_pin = board.D12  #DotStar
num_pixels = 12

# Uncomment the appropriate line below for NeoPixels or DotStar
pixels = neopixel.NeoPixel(data_pin,
#pixels = adafruit_dotstar(data_pin, clock_pin,
                            num_pixels,
                            brightness=0.2,
                            auto_write=False)
##########################################

comet = Comet(pixels, speed=0.05, color=(0,255,0), tail_length=5, bounce=True)


while True:
    comet.animate()