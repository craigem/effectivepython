#!/usr/bin/env python3

'''Item 15 from Effective Python'''


# Example 1
''' A common way to do this is to pass a helper function as the key argument to
a list's sort method. The helper's return value will be used as the value for
sorting each item in the list '''
print('Example 1:\n==========')

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


# Example 2
''' That function works for simple inputs '''
print('\nExample 2:\n==========')

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)


# Example 3
''' Why not also use the closure to flip a flag when high-priority items are
seen? Then the function can return the flag value after it's been modified by
the closure '''
print('\nExample 3:\n==========')

def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True  # Seems simple
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


# Example 4
''' run the function on the same inputs as before '''
print('\nExample 4:\n==========')

found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)


# Example 5
''' The nonlocal statement is used to indicate that scope traversal should
happen upon assignment for a specific variable name '''
print('\nExample 5:\n==========')


def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


# Example 6
''' When your usage of nonlocal starts getting complicated, it's better to wrap
your state in a helper class. Here, I define a class that achieves the same
result as the nonlocal approach '''
print('\nExample 6:\n==========')


class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
print('Found:', found)
print(numbers)
