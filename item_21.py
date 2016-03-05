#!/usr/bin/env python3

'''Item 21 from Effective Python'''


# Example 1
''' ignore OverflowError exceptions and return zero instead '''
print('Example 1:\n==========')

def safe_division(number, divisor, ignore_overflow, ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Example 2
''' This call will ignore the float overflow from division and will return zero
'''
print('\nExample 2:\n==========')

result = safe_division(1, 10**500, True, False)
print(result)


# Example 3
''' This call will ignore the error from dividing by zero and will return
infinity '''
print('\nExample 3:\n==========')

result = safe_division(1, 0, False, True)
print(result)


# Example 4
''' One way to improve the readability of this code is to use keyword
arguments '''
print('\nExample 4:\n==========')


def safe_division_b(number, divisor,
                  ignore_overflow=False,
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Example 5
''' Then callers can use keyword arguments to specify which of the ignore flags
they want to flip for specific operations, overriding the default behavior '''
print('\nExample 5:\n==========')

result = safe_division_b(1, 10**500, ignore_overflow=True)
print(result)
result = safe_division_b(1, 10**500, ignore_zero_division=True)
print(result)


# Example 6
''' In Python 3, you can demand clarity by defining your functions with
keyword-only arguments. These arguments can only be supplied by keyword, never
by position '''
print('\nExample 6:\n==========')


def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


# Example 7
''' Keyword arguments and their default values work as expected '''
print('\nExample 7:\n==========')

result = safe_division_c(1, 0, ignore_zero_division=True)
print(result)
