import paho.mqtt.client as mqtt
import time
 
 #Publisher:it sends humidity data with topic HumidityTopic at every 30 sec.I have used Paho as my mqtt client and eclipse as broker.
def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = mqtt.Client()
client.on_publish = on_publish
client.connect(“mqtt.eclipse.org”, 1883)
client.loop_start()

while True:
    humidity = random.randint(30,100)
    (rc, mid) = client.publish(“HumidityTopic”, str(humidity), qos=1)
    time.sleep(30)




