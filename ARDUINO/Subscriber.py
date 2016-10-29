from mosquitto import *
from serial import *
from random import *

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino
board = Serial("COM3",9600,timeout=2)

randomID = random()
client = Mosquitto("LightSubscriber" + str(randomID))
client.connect("10.212.61.136")
client.subscribe("/lights")

def messageRecieved (broker, obj, msg):
	global client
	payload = msg.payload.decode()
	print("Message " + msg.topic + " containing: " + payload)
	
client.on_message = messageRecieved

while (client != None): client.loop()
	




# The rest of your code goes in here !!!