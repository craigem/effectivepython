#!/usr/bin/env python3

'''Item 14 from Effective Python'''


# Example 1
'''In the case of dividing by zero, returning None seems natural because the
result is undefined '''
print('Example 1:\n==========')

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


# Example 2
''' Code using this function can interpret the return value accordingly. '''
print('\nExample 2:\n==========')

x, y = 6, 0
result = divide(x, y)
if result is None:
    print('Invalid inputs')


# Example 3
''' You may accidentally look for any False equivalent value to indicate errors
instead of only looking for None '''
print('\nExample 3:\n==========')

x, y = 0, 5
result = divide(x, y)
if not result:
    print('Invalid inputs')  # This is wrong!


# Example 4
''' The first part of the tuple indicates that the operation was a success or
failure.The second part is the actual result that was computed '''
print('\nExample 4:\n==========')

def divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


# Example 5
''' Callers of this function have to unpack the tuple. That forces them to
consider the status part of the tuple instead of just looking at the result of
division '''
print('\nExample 5:\n==========')

success, result = divide(x, y)
if not success:
    print('Invalid inputs')


# Example 6
''' The problem is that callers can easily ignore the first part of the tuple
(using the underscore variable name, a Python convention for unused variables).
The resulting code doesn't look wrong at first glance. This is as bad as just
returning None '''
print('\nExample 6:\n==========')

_, result = divide(x, y)
if not result:
    print('Invalid inputs')


# Example 7
''' The second, better way to reduce these errors is to never return None at
all. Instead, raise an exception up to the caller and make them deal with it
'''
print('\nExample 7:\n==========')

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


# Example 8
''' Now the caller should handle the exception for the invalid input case '''
print('\nExample 8:\n==========')

x, y, = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
