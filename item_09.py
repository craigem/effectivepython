#!/usr/bin/env python3

'''Item 9 from Effective Python'''


# Example 1
''' If the file is absolutely enormous or perhaps a never-ending network
socket, list comprehensions are problematic. Here, I use a list comprehension
in a way that can only handle small input values '''
print('Example 1:\n==========')
import random
with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('my_file.txt')]
print(value)


# Example 2
''' the generator expression immediately evaluates to an iterator and doesn't
make any forward progress '''
print('\nExample 2:\n==========')
it = (len(x) for x in open('my_file.txt'))
print(it)


# Example 3
''' The returned iterator can be advanced one step at a time to produce the
next output from the generator expression as needed (using the next built-in
function) '''
print('\nExample 3:\n==========')
print(next(it))
print(next(it))


# Example 4
''' take the iterator returned by the gen- erator expression above and use it
as the input for another generator expression '''
print('\nExample 4:\n==========')
roots = ((x, x**0.5) for x in it)
print(roots)


# Example 5
''' Each time I advance this iterator, it will also advance the interior
iterator, creating a domino effect of looping, evaluating conditional
expressions, and passing around inputs and outputs '''
print('\nExample 5:\n==========')
print(next(roots))
