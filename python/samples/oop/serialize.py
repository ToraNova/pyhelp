#!/usr/bin/python3

'''
serialization enables a class to be stored as a string, and further be
loaded (initialized) from the string: we wish to store the state of an object
in a serial manner (serializiation)
'''

class Foo:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ab = {'a':a, 'b':b}

    def do(self):
        print(self.a, self.b, self.ab)


if __name__ == "__main__":

    f = Foo(1, 2)
    f.do()
