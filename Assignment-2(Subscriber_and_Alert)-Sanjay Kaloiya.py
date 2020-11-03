import paho.mqtt.client as mqtt
import smtplib 

# Subscriber:it listens to HumidityTopic and checks if humidity value exceeds 80% if so happens it sends an email.

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("HumidityTopic")

def on_message(client, userdata, msg):
  if msg.payload.decode() >= 80: #checking for humidity range if>80%
  	 # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    # Authentication 
    s.login("sender_email_id", "sender_email_id_password")        
    message = "Humidity is above 80% please take proper action ASAP" 
    #sending alert Email
    s.sendmail("sender_email_id", "receiver_email_id", message)   
    s.quit() 
    
    client.disconnect()
    
client = mqtt.Client()
client.connect("mqtt.eclipse.org",1883)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()