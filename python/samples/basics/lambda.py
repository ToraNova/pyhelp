#!/usr/bin/python3

'''
python3 lambda functions
lambda functions are anonymous (no-name) functions that are only 1 line.
'''

# lambda <arg>: <function define>
foo = lambda a: print(a)
bar = lambda a, b: print(a,b)

foo(1)
bar(2,3)

# also can use args and kwargs
foo = lambda *args: print(*args)
bar = lambda *args, **kwargs: print(args,[(k, v) for k,v in kwargs.items()])

foo(1,2,3,4,5)
bar( 1,2,3, hello='world')

# even this is possible
(lambda *args: print(*args))('hi',',','I','am','a','lambda','function')
