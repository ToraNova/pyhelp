#!/usr/bin/python3

'''
python3 operators
'''

print(True and False)
print(True or False)
print(not True)

alst = [True, True, False]
blst = [1,2,3]

atst = False

# memory location comparison
print(False is False)
print(alst[2] is False)

print(all(alst)) #true only if all is true
print(any(alst)) #true is any is true
