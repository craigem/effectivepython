#!/usr/bin/env python3

'''Item 13 from Effective Python'''


# Example 1
''' One common usage of try / finally is for reliably closing file handles '''
print('Example 1:\n==========')

handle = open('random_data.txt', 'w', encoding='utf-8')
handle.write('success\nand\nnew\nlines')
handle.close()

handle = open('random_data.txt')  # May raise IOError
try:
    data = handle.read()  # May raise UnicodeDecodeError
finally:
    handle.close()        # Always runs after try


# Example 2
''' Use try / except / else to make it clear which exceptions will be handled
by your code and which exceptions will propagate up '''
print('\nExample 2:\n==========')

import json

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]         # May raise KeyError


# Example 3
''' Use try / except / else / finally when you want to do it all in one
compound statement '''
print('\nExample 3:\n==========')

UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')  # May raise IOError
    try:
        data = handle.read()   # May raise UnicodeDecodeError
        op = json.loads(data)  # May raise ValueError
        value = (
            op['numerator'] /
            op['denominator']) # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)   # May raise IOError
        return value
    finally:
        handle.close()         # Always runs
