from grovepi import *
import grovepi
import math
import time
# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 4  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the LED to digital port D4
# SIG,NC,VCC,GND


# Turn on LED once sensor exceeds threshold resistance
threshold = 700

grovepi.pinMode(light_sensor,"INPUT")

# Ultrasonic
ultrasonic = 3

while True:
    sensor_value = grovepi.analogRead(light_sensor)
    [temp,humidity] = grovepi.dht(sensor,blue)
    distance_value = ultrasonicRead(ultrasonic)
    print(sensor_value,temp,humidity,distance_value)
    time.sleep(1)
        
