# honeypi
Remote sensing of beehives

The following scripts are run on the ESP32 to pull readings from the sensor(s) and send them via MQTT:
- main.py
- ConnectWiFi.py
- dht_publish.py

The following scripts are run on a Raspberry Pi to pull and save the data from the MQTT server and to create plots from this data:
- mqtt_to_file.py
- create_plot.py


Acknowledgments
Thank you to https://www.rototron.info for providing a very useful tutorial on which the dht_publish.py script is based.
