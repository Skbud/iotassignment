# iotassignment
The assignment is done in two parts one for publishing and another for subscribing and alerting.


I have used Paho as my mqtt client and eclipse as my broker.

TheThe working as follows:


1.Publisher:It publishes message with topic humiditytopic every 30 second.The simulation for humidity sensor is done using python random function for simplicity.

2.Subscriber:It subscribed to topics humiditytopic.It then decodes the received  message which is then checked.If the received message value is greater than 80% an e-mail alert is generated.
