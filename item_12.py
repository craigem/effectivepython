#!/usr/bin/env python3

'''Item 12 from Effective Python'''


# Example 1
''' you can put an else block immediately after a loop’s repeated interior
block '''
print('Example 1:\n==========')

for  i in range(3):
    print('Loop %d' % i)
else:
    print('Else block!')


# Example 2
''' Using a break statement in a loop will actually skip the else block '''
print('\nExample 2:\n==========')

for i in range(3):
    print('Loop %d' % i)
    if i == 1:
        break
else:
    print('Else block!')


# Example 3
''' the else block will run immediately if you loop over an empty sequence '''
print('\nExample 3:\n==========')

for x in []:
    print('Never runs')
else:
    print('For Else block!')


# Example 4
''' The else block also runs when while loops are initially false '''
print('\nExample 4:\n==========')

while False:
    print('Never runs')
else:
    print('While Else block!')


# Example 5
''' The else block runs when the numbers are coprime because the loop doesn’t
encounter a break '''
print('\nExample 5:\n==========')

a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')


# Example 6
''' The first approach is to return early when you find the condition you’re
looking for '''
print('\nExample 6:\n==========')

def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

print(coprime(a, b))


# Example 7
''' The second way is to have a result variable that indicates whether you’ve
found what you’re looking for in the loop '''
print('\nExample 7:\n==========')

def coprime2(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

print(coprime2(a, b))
