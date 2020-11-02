#!/usr/bin/python3
'''
an example parent process to run child.py
using popen
a delay is noticeable because the child.py purposefully
delay its own execution
'''
import sys, time, subprocess

if __name__ == "__main__":
    childproc = subprocess.Popen(['./child.py','000'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        out,err = childproc.communicate(timeout=10)
        print("stdout:",out,"/ stderr:",err)
    except Exception as e:
        print("exception has occurred:",str(e))
        out,err = childproc.communicate()
        print("stdout:",out,"/ stderr:",err)
