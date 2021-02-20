# PyCascades2021
Materials and information for PyCascades 2021 Presentation

# Live Demo Resources
To follow along with the demo in real time, youll need:
  - A microcontroller with CircuitPython 6.0 installed (installation instructions here: <a href=https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython>https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython</a>)
  - An LED strip/string/matrix or a board (like Adafruit's <a href=https://www.adafruit.com/product/3333>CircuitPlayground Express</a>) with built-in LEDs
  - A Python coding environment - ideally one that can access the REPL, like <a href=https://codewith.mu/>the Mu code editor</a>
  - The CircuitPython led_animation libraries and dependencies. If you have CircuitPython 6.0 installed, you can download the ones you'll need directly from this repository. If you are working on an ATSAMD21 without extra flash memory (e.g Gemma M0 or Trinket M0), you should use the libraries in the minimal_led_animation_libraries folder so as not to fill all disk storage. Otherwise, use the libraries in the complete_led_animation_libraries folder. To install the libraries, simply copy them over to a folder named "lib" on the CIRCUITPY drive that appears when you plug in your board. 
