"""
Problem:
    This time we want to write calculations using functions and
    get the results. Let's have a look at some examples:

    There must be a function for each number from 0 ("zero") to 9 ("nine")

    There must be a function for each of the following mathematical 
    operations: plus, minus, times, divided_by

    Each calculation consist of exactly one operation and two numbers

    The most outer function represents the left operand, the most inner 
    function represents the right operand

    Divison should be integer division, e.g eight(divided_by(three)) 
    should return 2, not 2.666666...

    Examples:
        seven(times(five)) # must return 35
        four(plus(nine)) # must return 13
        eight(minus(three)) # must return 5
        six(divided_by(two)) # must return 3

>>> zero()
0

>>> one()
1

>>> two()
2

>>> three()
3

>>> four()
4

>>> five()
5

>>> six()
6

>>> seven()
7

>>> eight()
8

>>> nine()
9

>>> one(plus(one()))
2

>>> one(minus(one()))
0

>>> one(times(one()))
1

>>> one(divided_by(one()))
1

>>> two(plus(two()))
4

>>> one(plus(two()))
3
""" 

def switcher(number, operation):
    if operation[0] == 'plus':
        return number + operation[1]
    
    if operation[0] == 'minus':
        return number - operation[1]
    
    if operation[0] == 'times':
        return number * operation[1]
    
    if operation[0] == 'divided_by':
        return number // operation[1]


def zero():
    return 0

def one(operation=None):
    if not operation:
         return 1

    switcher(1, operation)
    
    # if not operation:
    #     return 1
    
    # if operation[0] == 'plus':
    #     return 1 + operation[1]
    
    # if operation[0] == 'minus':
    #     return 1 - operation[1]
    
    # if operation[0] == 'times':
    #     return 1 * operation[1]
    
    # if operation[0] == 'divided_by':
    #     return 1 // operation[1] 
    

def two(operation=None):
    if not operation:
        return 2
    
    if operation[0] == 'plus':
        return 2 + operation[1]
    
    if operation[0] == 'minus':
        return 2 - operation[1]
    
    if operation[0] == 'times':
        return 2 * operation[1]
    
    if operation[0] == 'divided_by':
        return 2 // operation[1]


def three():
    return 3


def four():
    return 4


def five():
    return 5


def six():
    return 6


def seven():
    return 7


def eight():
    return 8


def nine():
    return 9


def plus(number=None):
    return ('plus', number)


def minus(number=None):
    return ('minus', number)


def times(number=None):
    return ('times', number)


def divided_by(number=None):
    return ('divided_by', number)