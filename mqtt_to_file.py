import paho.mqtt.client as mqtt
import time

CLIENT_ID = "RPI Client"
SERVER = "127.0.0.1"
TOPIC = 'temp_humidity'
file = open("/home/pi/logs/mqtt.log", 'a')

client = mqtt.Client(CLIENT_ID) #Define MQTT Client

client.connect(SERVER) #Connect to MQTT Server

client.subscribe(TOPIC) #Subscribe to topic

def on_message(client, userdate, message): #Function activated on receiving message
	file.write(message.payload.decode("utf-8") + "\n")
	print("Message saved: ", str(message.payload.decode("utf-8")))

client.on_message=on_message #Attach function to on_message

client.loop_start() #Start client loop

time.sleep(4) #Delay to allow connection

client.loop_stop()

file.close()
