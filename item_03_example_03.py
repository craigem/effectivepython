#!/usr/bin/env python2.7

'''Item 3, example 3, from Effective Python'''


# Example 3
def to_unicode(unicode_or_str):
    '''In Python 2, you'll need one method that takes a str or unicode and
    always returns a unicode .'''
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value  # Instance of unicode

print(repr(to_unicode(u'foo')))
print(repr(to_unicode('foo')))
