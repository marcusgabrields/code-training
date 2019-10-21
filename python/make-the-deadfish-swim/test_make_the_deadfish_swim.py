"""Module to test deadfish parse."""
from string import ascii_lowercase

import pytest

from make_the_deadfish_swim import parse


@pytest.mark.parametrize(
    'letter',
    [l for l in ascii_lowercase if l not in ['i', 'd', 's', 'o']]
)
def test_can_accept_wrong_values(letter):
    """Test if the parse accepts wrong values."""
    assert parse(letter) == []


def test_can_parse_i_value():
    """Test if can parse 'i' value."""
    assert parse('i') == []


def test_can_parse_o_value():
    """Test if can parse 'o' value."""
    assert parse('o') == [0]


def test_can_parse_s_value():
    """Test if can parse 's' value."""
    assert parse('s') == []


def test_can_parse_d_value():
    """Test if can parse 'd' value."""
    assert parse('d') == []


def test_can_increments_value():
    """Test can increments value with 'i'."""
    assert parse('io') == [1]


def test_can_squares_value():
    """Test can squares value with 's'."""
    assert parse('iiso') == [4]


def test_can_decreace_value():
    """Test can squares value with 's'."""
    assert parse('iiddo') == [0]


def test_example():
    """Simple example."""
    print()
    assert parse('isoisoiso') == [1, 4, 25]


@pytest.mark.parametrize(
    'data, expected',
    [('iaoiiwero', [1, 3]),
     ('iisoddo', [4, 2]),
     ('iisso', [16])]
)
def test_parse_with_invalid_caracters(data, expected):
    """Parser must ignore invalid caracters."""
    assert parse(data) == expected
