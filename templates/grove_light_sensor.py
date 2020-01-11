import time
import grovepi

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0

# Connect the LED to digital port D4
# SIG,NC,VCC,GND


# Turn on LED once sensor exceeds threshold resistance
threshold = 700

grovepi.pinMode(light_sensor,"INPUT")

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value

        if resistance > threshold:
            # Send HIGH to switch on LED
            print("resistance supérieur au seuil")
        else:
            # Send LOW to switch off LED
            print("resistance inférieure au seuil")

        print("sensor_value = %d resistance = %.2f" %(sensor_value,  resistance))
        time.sleep(1)

    except IOError:
        print ("Error")
