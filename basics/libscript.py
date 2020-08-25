#!/usr/bin/python3

'''
python3 top-level names
'''

print("this will always run")
def somefunc(a=1):
    print('some func',a)

if __name__ == "__main__":
    # this is only executed
    # if this file is ran as a script
    print("running as a script")
