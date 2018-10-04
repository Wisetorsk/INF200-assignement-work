# -*- coding: utf-8 -*-
from median import median as m

"""
testing for median.py
"""


__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def test_empty():
    """
    Requesting the median of an empty list raises a ValueError exception.
    """
    print ('in test_empty')
    try:
        assert m([])
    except ValueError as err:
        print err


def test_correct():
    """
    Median function returns the correct value for a one-element list.
    """
    print ('in test_correct')
    assert m([2]) == 2


def test_unchanged():
    """
    Ensures that the median function leaves the original data unchanged.
    """
    print ('in test_unchanged')
    original = [3, 6, 5]
    real = [3, 6, 5]
    m(real)
    assert real == original


def test_tuple():
    """
    A test that ensures that the median function works for tuples and lists
    """
    print ('in test_tuple')
    toup = (1, 2, 3, 4, 5)
    assert m(toup) == 3


def test_mass():
    """
    Several tests that check that the correct median is returned for
    * lists with odd numbers of elements
    * lists with even numbers of elements
    * list with ordered, reverse-ordered and unordered elements
    """
    print ('in test_mass')
    odd = [2.0, 1.0, 4.0, 5.0, 3.0]
    even = [3.0, 6.0, 1.0, 2.0, 4.0, 5.0]
    order = [1.0, 2.0, 3.0, 4.0, 5.0]
    reverse = order[::-1]
    assert m(odd) == 3.0
    assert m(even) == 3.5
    assert m(order) == 3.0
    assert m(reverse) == 3.0
