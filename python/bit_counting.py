"""
Problem:
    Write a function that takes an integer as input,
    and returns the number of bits that are equal to 
    one in the binary representation of that number. 
    You can guarantee that input is non-negative.

    Example:
        The binary representation of 1234 is 10011010010, 
        so the function should return 5 in this case


>>> bit_counting(1234)
5

>>> bit_counting(10)
2

>>> bit_counting(452)
4
"""

def bit_counting(integer_number):
    bin_list = list(bin(integer_number))
    
    result = 0

    for element in bin_list:
        if element == '1': result += 1
    
    return result