# PyCascades2021
Materials and information for PyCascades 2021 Presentation

## Live Demo Resources
To follow along with the demo in real time, youll need:
  - A microcontroller running CircuitPython 6.0 (installation instructions here: <a href=https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython>https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython</a>)
  - An LED strip/string/matrix or a board (like Adafruit's <a href=https://www.adafruit.com/product/3333>CircuitPlayground Express</a>) with built-in LEDs
  - A Python coding environment like <a href=https://codewith.mu/>the Mu code editor</a>
  - The CircuitPython led_animation libraries and dependencies. If you have CircuitPython 6.0 installed, you can download just the libraries for the demo from this repository. There are two choices included:
    *  <b>bare_bones_led_animation_libraries</b> A minimal library bundle for use with an ATSAMD21 board without extra flash memory (e.g Gemma M0, Trinket M0 QtPy M0. Note that any board labelled "Express" *does* have extra flash)
    *  <b>complete_led_animation_libraries</b> A more comprehensive set of animation libraries for boards with a bit more memory
  - <b>AnimationBaseCode.py</b> Starter code for the animation demo
 
To install the animation libraries from this repository, drag the correct folder (bare_bones or complete) over to your CIRCUITPY drive and rename it to "lib".

## Interactive LED Sculpture
The sculptures in the background of my talk respond to tweets containing the hashtag <b>#pycascadesled</b> and <a href=https://htmlcolorcodes.com/color-names/>CSS color word</a> (words only, not RGB or HEX). The display colors will change to the color mentioned in the tweet after a three second delay. However, the talk may be streamed on a 20 second delay, so you may not see changes occur instantly.

## Additional CircuitPython LED Animation Resources
- <a href=https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel>Adafruit NeoPixel CircuitPython Learn Guide</a>
- <a href=https://learn.adafruit.com/circuitpython-led-animations>Adafruit CircuitPython LED Animation Guide</a>
- <a href=https://learn.adafruit.com/fancyled-library-for-circuitpython>Adafruit FancyLED Library Learn Guide</a> (FastLED analog for CircuitPython)
- <a href=https://learn.adafruit.com/infinity-mirror-collar>Adafruit Infinity Mirror Collar Learn Guide</a> This learn guide uses the led_animations libraries and bluetooth to build an interactive wearable infinity mirror collar
