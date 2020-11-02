#!/usr/bin/python3

'''
python3 sequences
these are mutable and are usually of homogenous datatypes
(string methods such as find, count works here as well)
'''

alst = [1,2,3,4,5,255,7,8,9]

# accessing
#print(alst[1])
#print(alst[-1])

# popping (alternative is in-place del)
aint = alst.pop()
bint = alst.pop(0)
del alst[1] # deletes in-place
#print(aint,bint,alst)

# concat
alst += [1,2,3]
#print(alst)

# reversing
#print(alst[::-1])
# or alst.reverse() (this is in-place)

# iteration
for i in alst:
    pass
    #print(i)

# cstyle
for i in range(len(alst)):
    pass
    #print(alst[i])

# enumrate with index
for i,j in enumerate(alst):
    pass
    #print(i,j)

for i,j in zip(alst,alst[::-1]):
    pass
    #print(i,j)

# sorting
for i in sorted(alst):
    pass
    #print(i)

for i in sorted(alst,reverse=True):
    pass
    #print(i)

# function mapping
def addone(a):
    return a+1

for i in map(addone, alst):
    pass
    #print(i)

# filtering
def lt4(a):
    if a < 4:
        return True
    else:
        return False

for i in filter(lt4, alst):
    #print(i)
    pass

# slicing
# start:end:step
print(alst[1:]) # slice first away
print(alst[:-1]) # slice last
print(alst[2:5]) # take only 2-5 element
print(alst[::2]) # take the element in even position

#min/max, length
print(max(alst)) #min(alst)
print(len(alst))

# other in-place methods (append, count, extend a.k.a concatenate)
alst.extend([999,999])
alst.append(123)
alst.insert(1,888) #insert 888 on position 1
alst.remove(2) #remove 2, matching first only
alst.sort() #in-place sorting, with similar effect to sorted()
print(alst)
