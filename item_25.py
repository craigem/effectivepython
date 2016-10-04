#!/usr/bin/env python3

'''Item 25 from Effective Python'''


# Example 1
''' The old way to initialize a parent class from a child class is to directly
call the parent class's __init__ method with the child instance '''

class MyBaseClass(object):
    def __init__(self,value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__self(self):
        MyBaseClass.__init__(self, 5)

# Example 2
''' define two parent classes that operate on the instance's value field '''

class TimesTwo(object):
    def __init__(self):
        self.value *= 2

class PlusFive(object):
    def __init__(self):
        self.value += 5

# Example 3
''' This class defines its parent classes in one ordering. '''

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

# Example 4
''' constructing it produces a result that matches the parent class ordering
'''
print('\nExample 4:\n==========')

foo = OneWay(5)
print('First ordering is (5 * 2) + 5 =', foo.value)

# Example 5
''' another class that defines the same parent classes but in a different
ordering '''

class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

# Example 6
''' I left the calls to the parent class constructors PlusFive.__init__ and
TimesTwo.__init__ in the same order as before, causing this class's behavior
not to match the order of the parent classes in its definition '''
print('\nExample 6:\n==========')

bar = AnotherWay(5)
print('Second ordering still is', bar.value)

# Example 7
''' define two child classes that inherit from MyBaseClass '''

class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5

class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2

# Example 8
''' define a child class that inherits from both of these classes, making
MyBaseClass the top of the diamond '''
print('\nExample 8:\n==========')

class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)

foo = ThisWay(5)
print('Should be (5 * 5) + 2 = 27 but is', foo.value)

# Example 9
''' In Python 3, you should always use super because it's clear, concise, and
always does the right thing '''
print('\nExample 9:\n==========')

class Explicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)

class Implicit(MyBaseClass):
    def __init__(self, value):
        super().__init__(value * 2)

assert Explicit(10).value == Implicit(10).value
