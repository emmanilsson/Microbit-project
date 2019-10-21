from microbit import *
import radio
import random
radio.on()
sensorID = 222

while True:
   sleep(100)
   temp = str(temperature())
   lightLevel = str(display.read_light_level())
   data = [sensorID, temp, lightLevel]
   radio.send(str(data))

   print(data)
