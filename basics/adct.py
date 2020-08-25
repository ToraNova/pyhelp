#!/usr/bin/python3

'''
python3 dictionaries
these are maps (they map one thing to another)
key-value pair
'''

adct = {1:1,2:4,3:9}

print(adct[1]) # you can use them like lists

bdct = {'a':1,'b':2,'c':3}
print(bdct['b'])

print([*bdct.keys()]) # * is the unpack operator for dict_keys

for i in bdct:
    print(i)

for i in bdct.keys():
    print(i)

for i in bdct.items():
    print(i)

for i in bdct.values():
    print(i)

def korder(a):
    # sort based on the first value
    return a[1]

bitm = bdct.popitem()

for i in sorted(bdct.items(), key=korder, reverse=True):
    print(i)

print(bitm)
