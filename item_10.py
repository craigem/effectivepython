#!/usr/bin/env python3

'''Item 10 from Effective Python'''


# Example 1
''' The range built-in function is useful for loops that iterate over a set of
integers. '''
print('Example 1:\n==========')
from random import randint
random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
print(random_bits)


# Example 2
''' When you have a data structure to iterate over, like a list of strings,
you can loop directly over the sequence '''
print('\nExample 2:\n==========')
flavour_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavour in flavour_list:
    print('%s is delicous' % flavour)


# Example 3
''' Often, you’ll want to iterate over a list and also know the index of the
current item in the list '''
print('\nExample 3:\n==========')
for i in range(len(flavour_list)):
    flavour = flavour_list[i]
    print('%d: %s' % (i + 1, flavour))


# Example 4
''' enumerate wraps any iterator with a lazy generator. This generator yields
pairs of the loop index and the next value from the iterator. The resulting
code is much clearer '''
print('\nExample 4:\n==========')
for i, flavour in enumerate(flavour_list):
    print('%d: %s' % (i + 1, flavour))


# Example 5
''' specify the number from which enumerate should begin counting '''
print('\nExample 5:\n==========')
for i, flavour in enumerate(flavour_list, 1):
    print('%d: %s' % (i, flavour))
