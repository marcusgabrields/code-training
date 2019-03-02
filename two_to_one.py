"""
Problem:
    Take 2 strings s1 and s2 including only letters from ato z. 
    Return a new sorted string, the longest possible, 
    containing distinct letters,

    each taken only once - coming from s1 or s2.

    Examples:
        a = "xyaabbbccccdefww"
        b = "xxxxyyyyabklmopq"
        longest(a, b) -> "abcdefklmopqwxy"

        a = "abcdefghijklmnopqrstuvwxyz"
        longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"



>>> longest('abc', 'def')
'abcdef'

>>> longest('def', 'ghi')
'defghi'

>>> longest('xyaabbbccccdefww', 'xxxxyyyyabklmopq')
'abcdefklmopqwxy'
"""

def longest(a, b):
    _list = '-'.join(a).split('-') + '-'.join(b).split('-')
    _list = list(set(_list))
    _list.sort()
    return ''.join(_list)

