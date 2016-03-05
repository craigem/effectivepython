#!/usr/bin/env python3

'''Item 20 from Effective Python'''


# Example 1
''' print logging messages that are marked with the time of the logged event
'''
print('Example 1:\n==========')

from datetime import datetime
from time import sleep


def log(message, when=datetime.now()):
    print('%s: %s' % (when, message))

log('Hi there!')
sleep(0.1)
log('Hi again!')


# Example 2
''' The convention for achieving the desired result in Python is to provide a
default value of None and to document the actual behavior in the docstring.
When your code sees an argument value of None , you allocate the default value
accordingly '''
print('\nExample 2:\n==========')


def log(message, when=None):
    """Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.now() if when  is None else when
    print('%s: %s' % (when, message))

log('Hi there!')
sleep(0.1)
log('Hi again!')


# Example 3
''' load a value encoded as JSON data. If decoding the data fails, you want an
empty dictionary to be returned by default '''
print('\nExample 3:\n==========')

import json


def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


# Example 4
''' The dictionary specified for default will be shared by all calls to decode
because default argument values are only evaluated once (at module load time).
This can cause extremely surprising behavior '''
print('\nExample 4:\n==========')

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)


# Example 5
''' The culprit is that foo and bar are both equal to the default parameter.
They are the same dictionary object '''
print('\nExample 5:\n==========')

assert foo is bar


# Example 6
''' The fix is to set the keyword argument default value to None and then
document the behavior in the function's docstring '''
print('\nExample 6:\n==========')


def decode(data, default=None):
    """ Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            DEfaults to an empty dictionary,
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
