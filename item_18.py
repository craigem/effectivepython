#!/usr/bin/env python3

'''Item 18 from Effective Python'''


# Example 1
''' say you want to log some debug information. With a fixed number of
arguments, you would need a function that takes a message and a list of values
'''
print('Example 1:\n==========')

def log(message, values):
    if not values:
        print(message)
    else:
        values_str =  ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', [1, 2])
log('Hi there', [])


# Example 2
''' The first parameter for the log message is required, whereas any number of
subsequent positional arguments are optional. The function body doesn't need to
change, only the callers do '''
print('\nExample 2:\n==========')

def log(message, *values):  # The only difference
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', 1 ,2)
log('Hi there')  # Much better


# Example 3
''' If you already have a list and want to call a variable argument function
like log , you can do this by using the * operator. This instructs Python to
pass items from the sequence as positional arguments '''
print('\nExample 3:\n==========')

favourites = [7, 33, 99]
log('Favourite colours', *favourites)


# Example 4
''' the variable arguments are always turned into a tuple before they are
passed to your function. This means that if the caller of your function uses
the * operator on a generator, it will be iterated until it's exhausted '''
print('\nExample 4:\n==========')

def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)


# Example 5
''' If you try to add a positional argument in the front of the argument list,
existing callers will subtly break if they aren't updated '''
print('\nExample 5:\n==========')

def log(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))


log(1, 'Favourites', 7, 33)         # New usage is OK
log('Favourite numbers', 7, 33)     # Old usage breaks
