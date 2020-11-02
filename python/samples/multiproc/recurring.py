#!/usr/bin/python3

from threading import Thread
from datetime import timedelta
import time

class Recurring(Thread):

    def __init__(self, interval, callback, magnitude = "s", *args, **kwargs):
        # initialize
        super().__init__()
        if(not callable(callback)):
            raise TypeError("callback not callable")
        self.callback = callback
        self.args = args
        self.kwargs = kwargs

        if(magnitude == "m"):
            self.delta = interval*60
        elif(magnitude == "h"):
            self.delta = interval*60*60
        elif(magnitude == "d"):
            self.delta = interval*60*60*24
        else:
            self.delta = interval

    def setargs(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def setcallback(self, callback):
        self.callback = callback

    def join(self):
        # override threading's join function
        self.stop()

    def run(self):
        self.running = True
        while(self.running):
            time.sleep(self.delta)
            self.callback(*self.args, **self.kwargs)

    def stop(self):
        self.running = False

def foo():
    print('test')

def bar(b):
    print(b)

if __name__ == "__main__":

    t0 = Recurring(0.5, foo)
    t1 = Recurring(1, bar, 's')
    t1.setargs('hello')
    t0.start()
    t1.start()
    time.sleep(5)
    t0.stop()
    t1.stop()
