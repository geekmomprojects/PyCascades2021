# CircuitPython LED Animation Demo base code for PyCascades 2021
# Bluetooth enabled demonstration
import board
import random
# Uncomment your LED type
import neopixel
#import adafruit_dotstar

#bluetooth
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

# Animation modules
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.color import colorwheel
from adafruit_led_animation.sequence import AnimationSequence

# Not enough memory for these on Gemma M0, Trinket M0, QTPy
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbow import Rainbow

##########################################
# SET THESE VALUES FOR YOUR BOARD and LEDS
data_pin = board.NEOPIXEL
#clock_pin = board.D12  #DotStar
num_pixels = 10

# Uncomment the appropriate line below for NeoPixels or DotStar
pixels = neopixel.NeoPixel(data_pin,
#pixels = adafruit_dotstar(data_pin, clock_pin,
                            num_pixels,
                            brightness=0.2,
                            auto_write=False)
##########################################

def switch_colors(anim):
    anim.color = colorwheel(random.randint(0,255))

comet = Comet(pixels, speed=0.03, color=(0,255,255), tail_length=6, bounce=False)
comet1 = Comet(pixels, speed=0.05, color=(255,255,0), tail_length=6, bounce=True)
rainbow = Rainbow(pixels, speed=0.1, period=2, step=10)
animations = AnimationSequence(comet, comet1, rainbow, advance_interval = 6)

comet.add_cycle_complete_receiver(switch_colors)
comet.notify_cycles = 2

ble = BLERadio()
uart_service = UARTService()
advertisement = ProvideServicesAdvertisement(uart_service)

while True:
    #advertise when not connected
    ble.start_advertising(advertisement)
    while not ble.connected:
        animations.animate()
    ble.stop_advertising()
    
    while ble.connected:
        animations.animate()
        if uart_service.in_waiting:
            packet = Packet.from_stream(uart_service)
            if isinstance(packet, ColorPacket):
                animations.color = packet.color
                animations.reset()