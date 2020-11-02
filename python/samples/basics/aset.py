#!/usr/bin/python3

'''
python3 sets
sets are lists that contains only unique elements
they are also unordered
'''

aset = {1,2,8,4}

print(aset)

for a in aset:
    print(a)

print( 1 in aset)
print( 3 in aset)

aset.add(9)
aset.add(0)

bset = {55, 1}

# equivalent to
#aset.union(bset)
aset.update(bset)
print(aset)

a = [1,2,2,3]
cset = set(a)
cset.remove(3)

try:
    cset.remove(3)
except Exception as e:
    print('Exception')

cset.discard(3)

print('we\'re still here')

cset.clear()

try:
    del aset
    print(aset)
except Exception as e:
    print(e)

aset = {1,2,3}
bset = {3,4,5}
cset = {3}
print( aset.intersection(bset) )
print( aset.isdisjoint(bset) )
print( cset.issubset(aset) )
print( bset.issuperset(cset) )
print( aset.difference(bset) ) # 1,2
print( bset.difference(aset) ) # 4,5
