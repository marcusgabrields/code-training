"""
Problem.

    Given a string of words, you need to find the highest scoring word.

    Each letter of a word scores points according to its position in the
    alphabet: a = 1, b = 2, c = 3 etc.

    You need to return the highest scoring word as a string.

    If two words score the same, return the word that appears earliest in the
    original string.

    *All letters will be lowercase and all inputs will be valid.*

    (start using pytest)
"""


def high(phrase: str) -> str:
    """Return a highest scoring word from a phrase."""
    splited_words = [word for word in phrase.split(' ') if word != '']

    if len(splited_words) == 1:
        return splited_words[0]

    scores = [score_word(w) for w in splited_words]
    highest_score = max(scores, key=int)

    for word in splited_words:
        if score_word(word) == highest_score:
            return word


def score_word(word):
    """Scores the word."""
    VALUES = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }

    score = 0
    for letter in word:
        score += VALUES[letter]

    return score
