# Timers and how to use them

from threading import Timer

def foo():
    print('delayed')

def bar(s):
    print(s)

if __name__ == "__main__":
    t0 = Timer(2.0, foo) #seconds, callback
    t1 = Timer(0.5, bar, 'shorter') #with args
    t0.start()
    t1.start()
