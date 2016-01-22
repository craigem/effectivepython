#!/usr/bin/env python3

'''Item 4 from Effective Python'''


# Example 1
from urllib.parse import parse_qs
MY_VALUES = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print('Example 1:\n==========')
print(repr(MY_VALUES))


# Example 2
print('\nExample 2:\n==========')
print('Red:     ', MY_VALUES.get('red'))
print('Green:   ', MY_VALUES.get('green'))
print('Opacity: ', MY_VALUES.get('opactity'))


# Example 3
# For query string 'red=5&blue=0&green='
RED = MY_VALUES.get('red', [''])[0] or 0
GREEN = MY_VALUES.get('green', [''])[0] or 0
OPACITY = MY_VALUES.get('opacity', [''])[0] or 0
print('\nExample 3:\n==========')
print('Red:     %r' % RED)
print('Green:   %r' % GREEN)
print('Opacity: %r' % OPACITY)


# Example 4
RED = int(MY_VALUES.get('red', [''])[0] or 0)
GREEN = int(MY_VALUES.get('green', [''])[0] or 0)
OPACITY = int(MY_VALUES.get('opacity', [''])[0] or 0)
print('\nExample 4:\n==========')
print('Red:     %r' % RED)
print('Green:   %r' % GREEN)
print('Opacity: %r' % OPACITY)


# Example 5
RED = MY_VALUES.get('red', [''])
RED = int(RED[0]) if RED[0] else 0
GREEN = MY_VALUES.get('green', [''])
GREEN = int(GREEN[0]) if GREEN[0] else 0
OPACITY = MY_VALUES.get('opacity', [''])
OPACITY = int(OPACITY[0]) if OPACITY[0] else 0
print('\nExample 5:\n==========')
print('Red:     %r' % RED)
print('Green:   %r' % GREEN)
print('Opacity: %r' % OPACITY)


# Example 6
RED = MY_VALUES.get('red', [''])
if RED[0]:
    RED = int(RED[0])
else:
    RED = 0

GREEN = MY_VALUES.get('green', [''])
if GREEN[0]:
    GREEN = int(GREEN[0])
else:
    GREEN = 0

OPACITY = MY_VALUES.get('opacity', [''])
if OPACITY[0]:
    OPACITY = int(OPACITY[0])
else:
    OPACITY = 0

print('\nExample 6:\n==========')
print('Red:     %r' % RED)
print('Green:   %r' % GREEN)
print('Opacity: %r' % OPACITY)


# Example 7
def get_first_int(values, key, default=0):
    '''Writing a helper function is the way to go, especially if you need to
    use this logic repeatedly.'''
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found


# Example 8
RED = get_first_int(MY_VALUES, 'red')
GREEN = get_first_int(MY_VALUES, 'green')
OPACITY = get_first_int(MY_VALUES, 'opacity')
print('\nExample 8:\n==========')
print('Red:     %r' % RED)
print('Green:   %r' % GREEN)
print('Opacity: %r' % OPACITY)
