#!/usr/bin/python3
import random
import datetime

"""
Given N gold, where each authentic gold weighs 10g, one of them is fake and weighs 9g
can you find the gold which weighs 9g
must be done within log2(n)
"""

def problem(n):
    goldarr = [10 for i in range(n)]
    goldarr[random.randint(0,n-1)] = 9
    return goldarr

def binsearch(arr):
    base = 0
    while 1:
        if len(arr) <= 1:
            return base
        stop = len(arr) // 2
        sum = 0
        for i in range(stop):
            sum += arr[i]
        if sum % 10 > 0:
            # cheap gold is in arr[0..stop]
            arr = arr[:stop]
        else:
            arr = arr[stop:]
            base += stop

if __name__ == "__main__":
    iter = 1000
    n = 10000
    avg = {'bin':0, 'lin':0}
    for i in range(iter):
        aGold = problem(n)
        s = datetime.datetime.now()
        i = binsearch(aGold)
        e = datetime.datetime.now()
        avg['bin'] += (e-s).microseconds

        if aGold[i] != 9:
            print('binary', i)

        s = datetime.datetime.now()
        for i,e in enumerate(aGold):
            if e == 9:
                break
        e = datetime.datetime.now()
        avg['lin'] += (e-s).microseconds
        
        if aGold[i] != 9:
            print('linear error', i)
    
    avg['bin'] /= iter
    avg['lin'] /= iter
    print(avg)
        