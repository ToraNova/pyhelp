#!/usr/bin/python3

'''
Laziness in Python by Prof Thorsten Altenkirch
https://www.youtube.com/watch?v=5jwV3zxXc8E
'''

# recursive
# generator of natural integer sequence
def nats(n):
    yield n # function will stop here on first call
    yield from nats(n+1) # continues here

def nrnats(n):
    st = n
    while(True):
        yield st
        st += 1

# takes in a sequence generator, and return the next prime
def sieve(s):
    n = next(s)
    yield n # return next prime
    # i for i in s # for every i in the sequence
    # if i%n != 0 # i is not a multiple of n
    # therefore, we pass the list of i which are NOT multiples of n
    # into the sieve again
    yield from sieve(i for i in s if i%n!=0)

# nats(2) -> 2,3,4,5 ...
# sieve(nats(2)) yield 2
# sieve(i for i in s if i%n!=0) # 3%2 != 0, 3 is first (removed 4,6,8,10...)
# yield 3
# sieve(i for i in s if i%n!=0) # 5%3 != 0, 5 is first (removed 9 ...)
# yield 5

# this is a generator which alternates between true and false
# outputting a false first
def bins(i):
    st = i # initialize state
    while(True):
        yield st # return state
        st = not st # flip

g = sieve(nats(2))
#print(next(g))
#print(next(g))
#print(next(g))

b = bins(False)
for i in range(10):
    if(next(b)):
        pass
        #print('1',end='')
    else:
        pass
        #print('0',end='')

def sawtooth(m, T):
    z = 0 # output state
    t = 0 # time state
    while(True):
        yield z
        t += 1
        if( t%T == 0 and t != 0):
            # period has occurred
            t = 0
            z = 0
        z += m

def triangle(i, m, T):
    z = i
    t = 0
    while(True):
        yield z
        t += 1
        if( t <= T/2):
            z += m
        else:
            z -= m
        if( t%T ==0 and t != 0):
            # period has occurred
            t = 0
            z = i

al = [0,1,2,1,0,-1,-2,-1,0]
# -2,-1,0,1,2,1,0,-1-2 -2, 1, -4, 2, -8, 4
al = triangle(-8,4,8)
for a in al:
    saw = triangle( a, 1,10)
    for j in range(30):
        z = next(saw)
        #print(z)
        for i in range(z):
            print('*',end='')
            pass
        print()
