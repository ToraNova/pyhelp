#!/usr/bin/python3

'''
python3 numerical datatype and operators
float assume the same form, just with decimal places
'''

aint = 255
bint = 3
cint = 240
dint = 15

# conversion to string
print(aint) #print the string representation
print(str(aint)) #convert then print
print(repr(aint)) #equivalent to above
print("%02X" % aint)
print("%f" % aint)

# arithmetic
print(aint+1)
print(aint-2)
print(aint*3)
print(aint/4)
print(int(aint/4))
print(aint % 2)
print(bint ** 2)
print(bint ** 0.5) # // is not square root, but floor division
print(bint // 2)

aint += 3 #likewise for -=, *= /= %= **= //=
print(aint)
aint -= 3

# equality/compare
print(aint >= bint) # <= also exist
print(aint < bint) # > also exist
print(aint == bint)
print(aint != bint) # equivalent to <>

# binary operation, b for binary, x for hex formatting
print("{:02x}".format(cint))
print("{:02x}".format(aint))
print("{:02b}".format(aint >> 1))
print("{:02b}".format(aint << 1))
print("{:02x}".format(aint & cint)) # binary AND
print("{:02x}".format(aint | cint)) # binary OR
print("{:02x}".format(~dint)) # binary negation
