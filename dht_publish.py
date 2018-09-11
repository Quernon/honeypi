import time
from umqtt.simple import MQTTClient
from machine import Pin
from dht import DHT22

def publish():
    SERVER = '192.168.0.13'  # MQTT Server Address (Change to the IP address of you$
    CLIENT_ID = 'ESP32_DHT22_Sensor'
    TOPIC = b'temp_humidity'
    client = MQTTClient(CLIENT_ID, SERVER)
    client.connect() # Connect to MQTT broker
    dht_running = True
    sensor = DHT22(Pin(15, Pin.IN, Pin.PULL_UP)) #DHT22 on GPIO 15 (input with internal pull up resistor)
    while dht_running:
        try:
            sensor.measure()   # Poll sensor
            t = sensor.temperature()
            h = sensor.humidity()
            tm = time.localtime(time.time())
            tmstr = '{:04d}-{:02d}-{:02d} {:02d}:{:02d}'.format(tm[0],tm[1],tm[2],tm[3],tm[4])
            print(tm)
            print(t, h, tm[0])
            if isinstance(t, float) and isinstance(h, float) and tm[0] > 2000:  # Confirm sensor results are numeric
                msg = (b'{0},{1:3.1f},{2:3.1f}'.format(tmstr, t, h))
                client.publish(TOPIC, msg, retain=True)  # Publish sensor data to MQTT topic
                print(str(msg))
                print('Sent to ' + SERVER + ' as ' + CLIENT_ID + '. Exiting.')
                client.disconnect()
                dht_running = False
            else:
                print('Invalid sensor readings.')
        except OSError:
            print('Failed to read sensor.')
        time.sleep(5)
