#!/usr/bin/env python3

'''Item 16 from Effective Python'''


# Example 1
''' Here, I accumulate results in a list using the append method and return it
at the end of the function '''
print('Example 1:\n==========')

def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])


# Example 2
''' A better way to write this function is using a generator '''
print('\nExample 2:\n==========')

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


result = list(index_words_iter(address))
print(result[:3])


# Example 3
''' I define a generator that streams input from a file one line at a time and
yields outputs one word at a time. The working memory for this function is
bounded to the maximum length of one line of input '''
print('\nExample 3:\n==========')

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

address_lines = """Four score and seven years
ago our fathers brought forth on this
continent a new nation, conceived in liberty,
and dedicated to the proposition that all men
are created equal."""

with open('address.txt', 'w') as f:
    f.write(address_lines)

from itertools import islice
with open('address.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))
