#!/usr/bin/env python3

'''Item 11 from Effective Python'''


# Example 1
''' List comprehensions make it easy to take a source list and get a derived
list by applying an expression '''
print('Example 1:\n==========')
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)


# Example 2
''' To iterate over both lists in parallel, you can iterate over the length of
the names source list '''
print('\nExample 2:\n==========')

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)


# Example 3
''' Using enumerate improves this slightly, but it’s still not ideal '''
print('\nExample 3:\n==========')

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)
print(max_letters)


# Example 4
''' The zip generator yields tuples containing the next value from each
iterator. The resulting code is much cleaner than indexing into multiple lists
'''
print('\nExample 4:\n==========')

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)
print(max_letters)


# Example 5
''' zip behaves strangely if the input iterators are of different lengths '''
print('\nExample 5:\n==========')

names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)
