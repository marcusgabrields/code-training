"""
Problem:
    Um isograma é uma palavra que não tem letras repetidas, consecutivas
    ou não consecutivas. Implemente uma função que determine se uma string que
    contém apenas letras é um isograma e retorne um booleano, indicando True
    para um isograma e False para não-isogramas.

    Suponha que a string vazia seja um isograma. Ignore o caso de letra
    (case insensitive).

     Exemplos:
        is_isogram("Dermatoglyphics" ) ==> True
        is_isogram("aba" )             ==> False
        is_isogram("mo0se" )           ==> False # existe um número



>>> is_isogram('')
True

>>> is_isogram('a')
True

>>> is_isogram('aa')
False

>>> is_isogram('8')
False

>>> is_isogram('abcd')
True

>>> is_isogram('abcda')
False

>>> is_isogram('Dermatoglyphics')
True

>>> is_isogram('mo0se')
False

>>> is_isogram('aA')
False

>>> is_isogram(2)
False

>>> is_isogram([1])
False
"""


def is_isogram(word):
    if not isinstance(word, str):
        return False

    word = word.lower()

    for letter in word:
        if letter.isdigit() or word.count(letter) != 1:
            return False

    return True
