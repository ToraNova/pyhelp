#!/usr/bin/python3

# quick reference on python tcp client
# this is a one-shot client (send something and terminates)
import socket

if __name__ == "__main__":
    # create the stream socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to addr:port
    try:
        s.connect(('127.0.0.1',13373))
        s.sendall(b'nihao')
        # s.send(msg) won't block until the entire message is sent, unlike s.sendall(msg)
    except ConnectionRefusedError:
        print('unable to connect to server.')
