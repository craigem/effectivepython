#!/usr/bin/env python3

'''Item 23 from Effective Python'''


# Example 1
''' sort a list of names based on their lengths by providing a lambda
expression as the key hook '''
print('Example 1:\n==========')

names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print (names)


# Example 2
''' define a hook that logs each time a key is missing and returns 0 for the
default value '''

def log_missing():
    print('Key added')
    return 0


# Example 3
''' Given an initial dictionary and a set of desired increments, cause the
log_missing function to run and print twice '''
print('\nExample 3:\n==========')

from collections import defaultdict

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
result = defaultdict(log_missing, current)
print('Before:', dict(result))
for key, amount in increments:
    result[key] += amount
print('After: ', dict(result))


# Example 4
''' define a helper function that uses a closure as the default value hook '''

def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # Stateful closure
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count


# Example 5
''' Running this function produces the expected result ( 2 ), even though the
defaultdict has no idea that the missing hook maintains state '''
print('\nExample 5:\n==========')

result, count = increment_with_report(current, increments)
assert count == 2
print(result)


# Example 6
''' defining a closure for stateful hooks is that it's harder to read than the
stateless function example. Another approach is to define a small class that
encapsulates the state you want to track '''

class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


# Example 7
''' Thanks to first-class functions, you can reference the CountMissing.missing
method directly on an object and pass it to defaultdict as the default value
hook '''
print('\nExample 7:\n==========')

counter = CountMissing()
result = defaultdict(counter.missing, current)  # Method ref

for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(result)


# Example 8
''' __call__ allows an object to be called just like a function. It also causes
the callable built-in function to return True for such an instance '''

class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()
assert callable(counter)


# Example 9
''' use a BetterCountMissing instance as the default value hook for a
defaultdict to track the number of missing keys that were added '''
print('\nExample 9:\n==========')

counter = BetterCountMissing()
result = defaultdict(counter, current)  # Relies on __call__
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
print(result)
