#!/usr/bin/env python3

'''Item 8 from Effective Python'''


# Example 1
''' simplify a matrix (a list containing other lists) into one flat list of all
cells.'''
print('Example 1:\n==========')
matrix = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)


# Example 2
''' square the value in each cell of a two-dimensional matrix. '''
print('\nExample 2:\n==========')
squared = [[x**2 for x in row] for row in matrix]
print(squared)


# Example 3
''' If this expression included another loop, the list comprehension would get
so long that you’d have to split it over multiple lines. '''
print('\nExample 3:\n==========')
my_lists = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
    ]
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2]
print(flat)


# Example 4
''' The indentation of this version makes the looping clearer than the list
comprehension. '''
print('\nExample 4:\n==========')
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)
print(flat)


# Example 5
''' to filter a list of numbers to only even values greater than four, these
two list comprehensions are equivalent '''
print('\nExample 5:\n==========')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
print('b: %s' % b)
print('c: %s' % c)


# Example 6
''' you want to filter a matrix so the only cells remaining are those divisible
by 3 in rows that sum to 10 or higher. Expressing this with list comprehensions
is short, but extremely difficult to read '''
print('\nExample 6:\n==========')
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]
print(filtered)
