#!/usr/bin/python3

'''
This is an auth mechanism with password/tls
TODO: incomplete example

chia_jason96@live.com
'''

import ssl
import paho.mqtt.client as mqtt

client = mqtt.Client()

# set username and password
client.username_pw_set(username = "cjason", password = "test123")

# set tls (username and password is worthless WITHOUT tls)
#client.tls_set( ca_certs = cafile, cert_reqs = ssl.CERT_REQUIRED, tls_version = ssl.PROTOCOL_TLS)
client.connect("localhost",1883)
