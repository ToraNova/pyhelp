#!/usr/bin/python3

'''
This demonstrates setting of Wills, which will be published upon death of a client
death meaning disconnection.

chia_jason96@live.com
'''
import paho.mqtt.client as mqtt

# defining callback on-connection
def on_connect(client, userdata, flags, rc):
    print("Connected with result code",rc)

if __name__ == "__main__":
    __willtopic = "test/will"
    __willmessg = "{\"status\":\"down\"}"
    host = "127.0.0.1"
    port = 1883
    timeout = 60

    #creates the mqtt client and attaches the callbacks
    client = mqtt.Client()
    client.on_connect = on_connect

    # set a will, publishes {"status":"down"} to test/will upon disconnection
    client.will_set( __willtopic, payload=__willmessg, qos=0, retain=True)

    #sets a userdata (most effectively a dictionary)
    client.connect(host,port,timeout)

    try:
        print("Hit Ctrl-C to publish will (you may need to setup a listener on %s)"%__willtopic)
        client.loop_forever() #blocking
        #client.loop_start() #non blocking
        #client.loop() #must be called multiple times to process data (polling)
    except KeyboardInterrupt:
        exit(0);
