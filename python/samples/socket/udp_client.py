#!/usr/bin/python3

# quick reference on python udp client
# this is a one-shot client (send something and terminates)
import socket

if __name__ == "__main__":
    # create the datagram socket (UDP)
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # send to addr:port message 'nihao'
    msg = b'nihao'
    s.sendto(msg,('127.0.0.1',13373))
