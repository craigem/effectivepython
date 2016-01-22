#!/usr/bin/env python3

'''Item 5 from Effective Python'''

import logging
from pprint import pprint
from sys import stdout as STDOUT


# Example 1
print('Example 1:\n==========')
a = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
print('First four:', a[:4])
print('Last four: ', a[-4:])
print('Middle two:', a[3:-3])


# Example 2
assert a[:5] == a[0:5]


# Example 3
assert a[5:] == a[5:len(a)]


# Example 4
print('\nExample 4:\n==========')
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])


# Example 5
a[:]      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:5]     # ['a', 'b', 'c', 'd', 'e']
a[:-1]    # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a[4:]     #                     ['e', 'f', 'g', 'h']
a[-3:]    #                          ['f', 'g', 'h']
a[2:5]    #           ['c', 'd', 'e']
a[2:-1]   #           ['c', 'd', 'e', 'f', 'g']
a[-3:-1]  #                          ['f', 'g']


# Example 6
print('\nExample 6:\n==========')
first_twenty_items = a[:20]
last_twenty_items= a[-20:]
print('First twenty items: %s' % first_twenty_items)
print('Last twenty items:  %s' % last_twenty_items)


# Example 7
print('\nExample 7:\n==========')
try:
    a[20]
except:
    logging.exception('Expected')
else:
    print('a[20] is: %s' % a[20])


# Example 8
print('\nExample 8:\n==========')
b = a[4:]
print('Before:    ', b)
b[1] = 99
print('After:     ', b)
print('No change: ', a)


# Example 9
print('\nExample 9:\n==========')
print('Before ', a)
a[2:7] = [99, 22, 14]
print('After ', a)


# Example 10
print('\nExample 10:\n==========')
b = a[:]
assert b == a and b is not a
print(b)


# Example 11
print('\nExample 11:\n==========')
b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b           # Still the same list object
print('After ', a)      # Now has different contents
