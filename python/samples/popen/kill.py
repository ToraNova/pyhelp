#!/usr/bin/python3

'''
kill.py is an attempt to kill a process with python
using popen, pgrep and kill
'''

from subprocess import Popen, PIPE

if __name__ == '__main__':
    pname = 'mosquitto'
    getpid = Popen(['pgrep',pname],stdout=PIPE)
    pid = getpid.stdout.readline()[:-1] #ignore the last character
    if(len(pid) > 0):
        term = Popen(['kill','-s','SIGTERM',pid])
        # use SIGKILL to have a more powerful kill effect
        # this is equivalent to doing
        # kill -s SIGTERM $(pgrep mosquitto)
        term.wait()
    else:
        print(f'{pname} not running')
