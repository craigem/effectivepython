#!/usr/bin/env python2.7

'''Item 3, example 4, from Effective Python'''


# Example 4
def to_str(unicode_or_str):
    '''You'll need another method that takes str or unicode and always returns
    a str.'''
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of str

print(repr(to_str(u'foo')))
print(repr(to_str('foo')))
