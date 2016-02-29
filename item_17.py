#!/usr/bin/env python3

'''Item 17 from Effective Python'''


# Example 1
''' You'd like to figure out what percentage of overall tourism each city
receives.  To do this you need a normalization function '''
print('Example 1:\n==========')

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)


# Example 2
''' I can reuse the same function later when I want to compute tourism numbers
for the whole world, a much larger data set '''
print('\nExample 2:\n==========')

path = 'my_numbers.txt'
with open(path, 'w') as f:
    for i in (15, 35, 80):
        f.write('%d\n' % i)

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)


# Example 3
''' If you iterate over an iterator or generator that has already raised a
StopIteration exception, you won't get any results the second time around '''
print('\nExample 3:\n==========')

it = read_visits('my_numbers.txt')
print(list(it))
print(list(it)) # Already exhausted


# Example 4
''' you can explicitly exhaust an input iterator and keep a copy of its entire
contents in a list. You can then iterate over the list version of the data as
many times as you need to. '''
print('\nExample 4:\n==========')

def normalize_copy(numbers):
    numbers = list(numbers)  # Copy the iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)


# Example 5
''' Copying the iterator could cause your program to run out of memory and
crash. One way around this is to accept a function that returns a new iterator
each time it's called '''
print('\nExample 5:\n==========')

def normalize_func(get_iter):
    total = sum(get_iter())     # New iterator
    result = []
    for value in get_iter():    # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result

percentages = normalize_func(lambda: read_visits(path))
print(percentages)


# Example 6
''' practically speaking you can achieve all of this behavior for your classes
by implementing the __iter__ method as a generator '''
print('\nExample 6:\n==========')

class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)


# Example 7
''' you can write your functions to ensure that parameters aren't just
iterators '''
print('\nExample 7:\n==========')

def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
normalize_defensive(visits)  # No error
visits = ReadVisits(path)
normalize_defensive(visits)  # No error


# Example 8
''' The function will raise an exception if the input is iterable but not a
container '''
print('\nExample 8:\n==========')

it = iter(visits)
normalize_defensive(it)
