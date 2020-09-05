#!/usr/bin/python3

'''
python3 string datatype
'''

astr = 'this is a string#'
bstr = '3'
cstr = '  whitespace    \n'
dstr = 'never going to give you up\nnever going to let you down'
estr = '{} {}'
fstr = '{a} {b}'
gstr = '{1} {0}'
hstr = '%.3f %s'

print(astr+bstr) #concatenation

# string partial matching
print(astr.startswith('this'))
print(astr.endswith('ing'))
print(astr.endswith('a'))

# conversion to int/float
bint = int(bstr)
bflt = float(bstr)
print(bint + 3, bflt / 2.3)

# there exist left and right versions of strip
print(cstr.strip())
print(cstr.strip('\n'))
print(astr.strip('t'))

# string splitting
print(dstr)
print(dstr.splitlines())
print(dstr.split('e'))

# string joining
print("".join( [astr, bstr, gstr] ))

# string checking
print(bstr.isdecimal())
print(astr.islower())
print(astr.isupper())
print(astr.isalpha()) #isalnum (alphanumeric), isnumeric
print(astr.isprintable()) #

# formatting
print(estr.format(3,'pigs'))
print(fstr.format(a=4, b='cats'))
print(gstr.format('cows',5)) #notice the reverse order
print(hstr % (6,'donkeys')) #alternative syntax

# finding and counting
# find v in dstr, this shud print 2 as it is the index
print(dstr.find('v')) # equivalent to dstr.index('v')
print(dstr.rfind('v')) # find from the right
print(dstr.count('v')) #count occurences of v in dstr

wstr = b'\x30\x31\x00\x20\x61\x41'
print(wstr)
print(ascii(wstr)) # replaces unprintable char with escape seq

# misc
print(astr.swapcase())

print(ord('a')) #print ascii value
print(chr(97)) # chr converts int to an ascii char

