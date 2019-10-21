from microbit import *
import radio
import random
radio.on()

while True:
   sleep(100)
   temp = temperature()
   lightLevel = display.read_light_level()
   data = radio.receive()
   print(data)
