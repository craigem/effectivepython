#!/usr/bin/env python3

'''Item 6 from Effective Python'''

import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
'''stride makes it easy to group by even and odd indexes in a list'''
print('Example 1:\n==========')
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)


# Example 2
'''a common Python trick for reversing a byte string is to slice the
string with a stride of -1'''
print('\nExample 2:\n==========')
x = b'mongoose'
y = x[::-1]
print(y)


# Example 3
''' it will break for Unicode characters encoded as UTF-8 byte strings '''
'''print('\nExample 3:\n==========')
w = '謝謝'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')'''


# Example 4
''' Are negative strides besides -1 useful? '''
print('\nExample 4:\n==========')
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])
print(a[::-2])


# Example 5
''' What do you think 2::2 means? What about -2::-2 vs. -2:2:-2 vs.
2:2:-2 ? '''
print('\nExample 5:\n==========')
print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])


# Example 6
''' If you must use stride with start or end indexes, consider using one
assignment to stride and another to slice. '''
print('\nExample 6:\n==========')
b = a[::2]
c = b[1:-1]
print(b)
print(c)
