"""
Problem:
    Write a function that takes in a string of one or 
    more words, and returns the same string, but with 
    all five or more letter words reversed. Strings passed in 
    will consist of only letters and spaces. Spaces 
    will be included only when more than one word is present.

    Examples:
        spin_words( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
        spin_words( "This is a test") => returns "This is a test" 
        spin_words( "This is another test" )=> returns "This is rehtona test"


>>> spin_words('Hey fellow warriors')
'Hey wollef sroirraw'

>>> spin_words('This is a test')
'This is a test'

>>> spin_words('This is another test')
'This is rehtona test'
"""

# TODO: Can be more simple?
def spin_words(word):
    spinned_word = ''
    for cont, w in enumerate(word.split()):
        if len(w) >= 5:
            spinned_word += w[::-1]
        else:
            spinned_word += w
        
        if cont < len(word.split()) - 1:
            spinned_word += ' '

    return spinned_word