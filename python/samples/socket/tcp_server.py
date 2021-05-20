#!/usr/bin/python3

# quick reference on python tcp server
# this is a one-shot server (recv something and terminates)
import socket

if __name__ == "__main__":
    # create the stream socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind socket to ipv4 address:port
    s.bind(('127.0.0.1',13373))
    # start listening on bound addr:port
    s.listen()
    # accept incoming connection
    conn, addr = s.accept()
    msg = conn.recv(1024) # receive at most 1024 from conn
    print('recv %s from %s' %(msg, addr))
