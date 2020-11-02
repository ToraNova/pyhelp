#!/usr/bin/python3

'''sample of opening a file for writing'''
import time

if __name__ == "__main__":

    '''
    opens a file 'file_write.txt' in some modes:
    w - write
    r - read
    b - binary
    t - text
    a - append
    + - r/w

    an optional 3rd arg 0 at the end is to disable bufferring
    (this causes the file to be written instantly
    alternatively, a flush can be used outfile.flush() to force
    the buffer to be written into the file
    '''
    with open("file_write.txt",'r') as infile:
        lines = infile.readlines() #arg: max number of bytes
        lines = [l[:-1] for l in lines] # strip the final char (\n)

    for l in lines:
        print(l)

    print('---------------------------------')

    with open("file_write.txt",'r') as infile:
        ct = infile.read() #arg: max number of bytes
        ct = ct[:-1] # strip the final char (\n)
    print(ct)


