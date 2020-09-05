#!/usr/bin/python3

'''
python3 tuples. they're not that different from list
but the consensus and culture is that (not a must)
list: homogenous (same type)
tuple: heterogenous (diff type)

THE MAIN DIFFERENCE is that tuples are FIXED size,
and therefore faster
tuples are ordered and immutable
'''

atpl = (1,2,'a diff type')
btpl = atpl * 5

for i in btpl:
    print(i)

ctpl = (4,5) + atpl

for i in ctpl:
    print(i)

