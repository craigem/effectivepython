#!/usr/bin/env python3

'''Item 7 from Effective Python'''


# Example 1
''' you want to compute the square of each number in a list. You can do this
by providing the expression for your computation and the input sequence to
loop over '''
print('Example 1:\n==========')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)


# Example 2
''' map requires creating a lambda function for the computation, which is
visually noisy. '''
print('\nExample 2:\n==========')
squares = map(lambda x: x ** 2, a)
print(squares)


# Example 3
''' say you only want to compute the squares of the numbers that are divisible
by 2 '''
print('\nExample 3:\n==========')
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)


# Example 4
''' filter built-in function can be used along with map to achieve the same
outcome, but it is much harder to read '''
print('\nExample 4:\n==========')
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
assert even_squares == list(alt)
print(even_squares)


# Example 5
''' Dictionaries and sets have their own equivalents of list comprehen-
sions. These make it easy to create derivative data structures when
writing algorithms. '''
print('\nExample 5:\n==========')
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)
