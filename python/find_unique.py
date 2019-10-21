"""
Problem:
    There is an array with some numbers. All numbers are equal except for one. Try to find it!

    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    It’s guaranteed that array contains more than 3 numbers.


>>> find_uniq([1, 2, 2])
1

>>> find_uniq([2, 1, 1])
2

>>> find_uniq([1, 2, 1])
2

>>> find_uniq([2, 1, 2])
1

>>> find_uniq([1, 1, 2])
2

>>> find_uniq([2, 2, 1])
1

>>> find_uniq([2, 2, 1, 2])
1

>>> find_uniq([1, 2, 2, 2])
1

>>> find_uniq([2, 2, 2, 1])
1
"""

def find_uniq(arr):
    first, second, third = arr[0], arr[1], arr[2]

    if first != second and first != third:
        return first
    
    if second != first and second != third:
        return second
    
    if third != first and third != second:
        return third
    
    repeated = first

    for element in arr:
        if element != repeated:
            return element