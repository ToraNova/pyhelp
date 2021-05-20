#!/usr/bin/python3

# quick reference on python udp server
# this is a one-shot server (receive something and terminates)
import socket

if __name__ == "__main__":
    # create the datagram socket (UDP)
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # bind socket to ipv4 address:port
    s.bind(('127.0.0.1',13373))

    msg, addr = s.recvfrom(1024)
    print('recv %s from %s' %(msg, addr))
