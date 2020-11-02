#!/usr/bin/python3

'''
an example child process to be run by parent.py
'''

import sys, time

if __name__ == "__main__":
    if(len(sys.argv)>1):
        arg1 = sys.argv[1]
        print(arg1)
    time.sleep(1) # sleep to demonstrate child process makes the parent wait
    print('done')
    exit(0)


