def connect():
    import network
    from time import sleep

    ssid = "XXXX"
    password =  "YYYY"
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        station.connect(ssid, password)
	sleep(2)
 
    print("Connection successful")
    print(station.ifconfig())
