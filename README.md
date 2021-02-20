# PyCascades2021
Materials and information for PyCascades 2021 Presentation

## Live Demo Resources
To follow along with the demo in real time, youll need:
  - A microcontroller with CircuitPython 6.0 installed (installation instructions here: <a href=https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython>https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython</a>)
  - An LED strip/string/matrix or a board (like Adafruit's <a href=https://www.adafruit.com/product/3333>CircuitPlayground Express</a>) with built-in LEDs
  - A Python coding environment like <a href=https://codewith.mu/>the Mu code editor</a>
  - The CircuitPython led_animation libraries and dependencies. If you have CircuitPython 6.0 installed, you can download them directly from this repository. There are two options:
    *  A bare bones library bundle for you are working on an ATSAMD21 without extra flash memory (e.g Gemma M0 or Trinket M0. Any board with the label "Express" has extra flash.
    *  A complete_led_animation_libraries folder for other boards with more memory
 
To install the animation libraries from this repository, drag the correct folder (bare_bones or complete) over to your CIRCUITPY drive and rename it to "lib".

## Interactive LED Sculpture
The sculptures in the background of my talk respond to tweets containing the hashtag <b>#pycascadesled</b> and <a href=https://htmlcolorcodes.com/color-names/>CSS color word</a> (words only, not RGB or HEX). The display colors will change to the color mentioned in the tweet after a three second delay. However, the talk may be streamed on a 20 second delay, so you may not see changes occur instantly.

## Additional Resources
- <a href=https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel>Adafruit's NeoPixel CircuitPython Learn Guide</a>
- <a href=https://learn.adafruit.com/circuitpython-led-animations>Adafruit's CircuitPython LED Animation Guide</a>
