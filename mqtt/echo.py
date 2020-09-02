#!/usr/bin/python3

'''
This is an echo-back mqtt client
listens to topicA, and echoes back whatever it receives to topicB

chia_jason96@live.com
'''
import paho.mqtt.client as mqtt

# defining callback on-connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code",rc)
    #subscribe and listen to topic A
    client.subscribe(userdata.get("topicA"))
    print("Listening on:",userdata.get("topicA"))

#defining callback behavior upon message receive
def echo_message(client, userdata, msg):
    # republish to topic B
    client.publish(userdata.get("topicB"),msg.payload)
    print("Echo:",userdata.get("topicB"),msg.payload)

if __name__ == "__main__":
    __topicA = "ping/all"
    __topicB = "reply/all"
    host = "127.0.0.1"
    port = 1883
    timeout = 60

    # userdata allows easy control of the mqtt client
    udat = {"topicA":__topicA, "topicB":__topicB}

    #creates the mqtt client and attaches the callbacks
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = echo_message

    #sets a userdata (most effectively a dictionary)
    client.user_data_set(udat)
    client.connect(host,port,timeout)

    try:
        client.loop_forever() #blocking
        #client.loop_start() #non blocking
        #client.loop() #must be called multiple times to process data (polling)
    except KeyboardInterrupt:
        exit(0);
