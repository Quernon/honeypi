import ConnectWiFi #Script to connect to WiFi. SSID and password must be set.
import time
import machine
from ntptime import settime
import dht_publish #Script to send signals from DHT22 sensor to mqtt server.

ConnectWiFi.connect() #Connect to WiFi
time.sleep(0.5)

settime() #Retrieve time from internet

led = machine.Pin(2, machine.Pin.OUT)

#Blinks to indicate that connection to WiFi is succesful.
counter = 0
while counter < 3:
    led.value(1)
    time.sleep(0.1)
    led.value(0)
    time.sleep(0.1)
    counter += 1

#Main loop. One second LED blink on each loop.
while True:
    dht_publish.publish()
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(900)
