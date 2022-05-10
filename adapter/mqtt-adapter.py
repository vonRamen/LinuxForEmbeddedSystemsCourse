import paho.mqtt.client as mqtt
from pymongo import MongoClient
import time    

client = MongoClient('localhost', 27017)
db = client["data"]

def handle_message(topic, payload):
    col = db[topic]
    timestamp = int(time.time())
    values = {"Test": "Test", "message": payload, "timestamp": timestamp}

    x = col.insert_one(values)
    

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("smart_alarm/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    val = float(msg.payload)
    handle_message(msg.topic, val)

    print(msg.topic+" "+str(val))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("kristian", "1234")

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()