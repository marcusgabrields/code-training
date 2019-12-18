"""Problem: Write a function that accepts an array of 10 integers 
   (between 0 and 9), that returns a string of those numbers in the 
   form of a phone number.
"""
def create_phone_number(n):
   """
   >>> create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
   '(123) 456-7890'

   >>> create_phone_number([1, 7, 6, 5, 3, 9, 8, 7, 6, 5])
   '(176) 539-8765'
   """
   n = ''.join(str(x) for x in n)
   return f'({n[0:3]}) {n[3:6]}-{n[6:10]}'


if __name__ == '__main__':
    import doctest
    doctest.testmod()