#!/usr/bin/python3

from threading import Thread, Event

class EventThread(Thread):

    # example setup function
    # returns a value to be stored
    def default_setup(par):
        return 1

    # example callback function
    # returns a value to be stored
    def default_callback(store, msg):
        print("msg avail: %s, store: %s" % (str(msg), str(store)))
        return 1

    def __init__(self, setup=default_setup, callback=default_callback):
        # initialize
        super().__init__()
        self._kille = Event() # stopping event. flag for stop
        self._active = Event() # pause an event, disallowing messages
        self._msgae = Event() # message passing event.

        # clear the flag
        self._kille.clear()
        self._msgae.clear()
        self._active.set()
        self._callback = callback
        self._setup = setup
        self._store = None # this is for storage

    # thread controls
    def kill(self):
        # kills the thread
        self._kille.set()
        self._active.set()

    def pause(self):
        self._active.clear()

    def unpause(self):
        self._active.set()

    def pushmsg(self, msg):
        # allows external process to pass a msg onto the thread
        self.msg = msg
        # sets the flag to indicate a message is available
        self._msgae.set()

    def setup(self, par):
        self._store = self._setup(par)

    def run(self):
        try:
            while not self._kille.is_set():
                self._active.wait() # only continue if thread is active
                self._msgae.wait() # threading block mechanism
                if( self._kille.is_set() ):
                    break
                self._store = self._callback(self._store, self.msg)
                self._msgae.clear() # make it stop after processing the msg
        except Exception as e:
            print("exception has occurred:",e)
        finally:
            print("thread stopped")

if __name__ == "__main__":
    # sample thread to count up upon message integer
    def sample_setup(par):
        # sample starts from 0
        return par

    def sample_callback_a(store, msg):
        while(msg>0):
            store += 1
            msg -= 1
            print('a',store)
            time.sleep(1)
        return store

    def sample_callback_b(store, msg):
        while(msg>0):
            store += 1
            msg -= 1
            print('b',store)
            time.sleep(0.2)
        return store

    import time

    eta = EventThread(sample_setup, sample_callback_a)
    etb = EventThread(sample_setup, sample_callback_b)
    eta.setup(0)
    etb.setup(-2)
    eta.start()
    etb.start()

    eta.pushmsg(3)
    etb.pushmsg(16)
    print('main thread is free again')
    time.sleep(1)
    time.sleep(1)
    try:
        eta.join()
        etb.join()
    except KeyboardInterrupt:
        print('terminating thread a')
        eta.kill()
        eta.pushmsg(0)
        eta.join()
        etb.kill()
        etb.pause()
        etb.pushmsg(0)
        time.sleep(1)
        etb.unpause()
        etb.join()
    print('main thread ended')
