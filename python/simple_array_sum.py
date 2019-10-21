"""
Problem:
    Given an array of integers, find the sum of its elements.
    For example, if the array a = [1, 2, 3], 1 + 2 + 3 = 6 , so return 6.


>>> simple_array_sum([1, 2, 3])
6

>>> simple_array_sum([-1, -1, -1])
-3

>>> simple_array_sum([10, -10, 0])
0
"""

def simple_array_sum(array):
    result = 0

    for element in array:
        result += element
    
    return result
