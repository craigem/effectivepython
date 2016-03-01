#!/usr/bin/env python3

'''Item 19 from Effective Python'''


# Example 1
''' calling a function in Python allows for passing arguments by position '''
print('Example 1:\n==========')

def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6


# Example 2
''' The keyword arguments can be passed in any order as long as all of the
required positional arguments are specified. You can mix and match keyword and
positional arguments. These calls are equivalent '''
print('\nExample 2:\n==========')

remainder(20, 7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)


# Example 3
''' compute the rate of fluid flowing into a vat. If the vat is also on a
scale, then you could use the difference between two weight measurements at two
different times to deter- mine the flow rate '''
print('\nExample 3:\n==========')

def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print('%.3f kg per second' % flow)


# Example 4
''' it'd be helpful to use the last sensor measurements to approximate larger
time scales, like hours or days. You can provide this behavior in the same
function by adding an argument for the time period scaling factor '''
print('\nExample 4:\n==========')

def flow_rate(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff, 1)
print('Flow per second: %s kg' % flow_per_second)


# Example 5
''' To make this less noisy, I can give the period argument a default value '''
print('\nExample 5:\n==========')

def flow_rate(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate(weight_diff, time_diff)
flow_per_hour = flow_rate(weight_diff, time_diff, period=3600)
print('Flow per second: %s kg' % flow_per_second)
print('Flow per hour: %s kg' % flow_per_hour)


# Example 6
''' extend the flow_rate function above to calculate flow rates in weight units
besides kilograms '''
print('\nExample 6:\n==========')

def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

pounds_per_hour = flow_rate(weight_diff, time_diff, period=3600,
                            units_per_kg=2.2)


# Example 7
''' The only problem with this approach is that optional keyword ­arguments
like period and units_per_kg may still be specified as positional arguments '''
print('\nExample 7:\n==========')

pounds_per_hour = flow_rate(weight_diff, time_diff, 3600, 2.2)
