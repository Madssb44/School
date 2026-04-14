import paho.mqtt.client as paho 
from paho import mqtt  
import json 

data_dict = {"classes":"ITEK 2ed",
             "classes/tables":"4",
             "classes/tabels/names":"andreas, mads, mads"}

client = paho.Client(client_id="tester", userdata=None, protocol=paho.MQTTv5)
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set("Zaarey", "Eaaamb123")

client.connect("28a8f8567d4a4cc18721870ec47abd19.s1.eu.hivemq.cloud", 8883)
client.on_publish=lambda *x:print(*x)
for topic, value in data_dict.items():
    client.publish(topic, payload=str(value), qos=0)


client.disconnect()

