#!/usr/bin/python3

'''
This is an echo-back mqtt client
listens to topicA, and echoes back its ID to topicB

THIS IS A SLIGHTLY MODIFIED VERSION OF echo.py to echo back an ID
in JSON format (designed for a heartbeat system), serving as an
example on how HOST should reply to heartbeat pings

chia_jason96@live.com
'''
import paho.mqtt.client as mqtt

# defining callback on-connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code",rc)
    client.subscribe(userdata.get("topicA")) #subscribe to topic A
    print("Listening on:",userdata.get("topicA"))

# defining callback behavior upon message receive
# the use of user-data is completely optional, and one may
# choose read a global ID variable instead.
def echo_message(client, userdata, msg):
    # direct & simple way, where 1 is a hard-coded or global var.
    #re_json = "{\"id\":1}"
    # userdata method, more sophistication
    re_json = "{\"id\":%d}" % (userdata.get("hostID"))
    # republish to topic B, with ID in json format
    client.publish(userdata.get("topicB"), re_json)
    print("Echo:",userdata.get("topicB"), re_json)

if __name__ == "__main__":
    __topicA = "ping/all"
    __topicB = "reply/all"
    __hostID = 1
    host = "127.0.0.1"
    port = 1883
    timeout = 60

    # userdata allows easy control of the mqtt client
    udat = {"topicA":__topicA, "topicB":__topicB, "hostID":1}

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
