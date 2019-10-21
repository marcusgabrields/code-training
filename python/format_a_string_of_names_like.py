"""
Problem:
    Given: an array containing hashes of names

    Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

    Example:

        namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
        # returns 'Bart, Lisa & Maggie'

        namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
        # returns 'Bart & Lisa'

        namelist([ {'name': 'Bart'} ])
        # returns 'Bart'

        namelist([])
        # returns ''
        
    Note: all the hashes are pre-validated and will only contain A-Z, a-z, '-' and '.'.



>>> namelist([])
''

>>> namelist([{'name': 'Bart'}])
'Bart'

>>> namelist([{'name': 'Bart'}, {'name': 'Lisa'}])
'Bart & Lisa'

>>> namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])
'Bart, Lisa & Maggie'
"""

def namelist(names):
    if len(names) == 0:
        return str('')

    if len(names) == 1:
        return names[0]['name']
    
    if len(names) == 2:
        return '{} & {}'.format(names[0]['name'], names[1]['name'])

    result = ''
    cont = 0

    while cont < len(names) - 2:
        result += '{}, '.format(names[cont]['name'])
        cont += 1

    result += '{} & {}'.format(names[-2]['name'], names[-1]['name'])
    return result