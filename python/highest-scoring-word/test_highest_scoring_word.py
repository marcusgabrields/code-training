"""Module to test highest_scoring_word.py."""
import pytest

from highest_scoring_word import high, score_word


@pytest.mark.skip('Obsolete test')
def test_can_call_high():
    """Test if high function can be called."""
    assert high() is None


def test_simple_word():
    """Test a simple string."""
    assert high('feijoada') == 'feijoada'


def test_two_words_phrase():
    """Test a two words phrase."""
    assert high('a b') == 'b'


def test_a_score():
    """Test score_word with a one caracter string."""
    assert score_word('a') == 1


def test_b_score():
    """Test score_word with v one caracter string."""
    assert score_word('b') == 2


@pytest.mark.parametrize(
    'letter, expected',
    [('a', 1),
     ('b', 2),
     ('c', 3),
     ('d', 4),
     ('e', 5),
     ('f', 6),
     ('g', 7),
     ('h', 8),
     ('i', 9)]
)
def test_all_letters_from_alphabet(letter, expected):
    """Test all letters."""
    assert score_word(letter) == expected


def test_score_of_feijoada():
    """Test the score of word 'feijoada'."""
    assert score_word('feijoada') == 51


@pytest.mark.parametrize(
    'phrase, expected',
    [('man i need a taxi up to ubud', 'taxi'),
     ('what time are we climbing up the volcano', 'volcano'),
     ('take me to semynak', 'semynak'), ]
)
def test_complexes_examples(phrase, expected):
    """Test some complexes examples."""
    assert high(phrase) == expected
