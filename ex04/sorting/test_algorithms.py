# -*- coding: utf-8 -*-
from bubble_sort import bubble_sort as b
"""

"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def test_empty():
    """Test that the sorting function works for empty list"""
    print ('in test_empty')
    assert b([]) == []


def test_single():
    """Test that the sorting function works for single-element list"""
    print ('in test_single')
    assert b([1]) == [1]


def test_sorted_is_not_original():
    """Test that the sorting function returns a new object."""
    print ('in test_sorted_is_not_original')
    test = [1, 2, 3]
    copy = test
    assert b(test) is not copy


def test_original_unchanged():
    """Test that sorting leaves the original data unchanged."""
    print ('in test_original_unchanged')
    original = [3, 6, 5]
    real = [3, 6, 5]
    assert b(real) is not original


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    print ('in test_sort_sorted')
    sort = [1, 2, 3, 4, 5]
    rel = [1, 2, 3, 4, 5]
    assert b(sort) == rel


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    print ('in test_sort_reversed')
    data = [1, 2, 3, 4, 5]
    reverse = data[::-1]
    assert b(reverse) == data


def test_sort_allequal():
    """Test that sorting handles data with identical elements."""
    print ('in test_sort_allequal')
    data = [1, 1, 1, 1, 1]
    rel = [1, 1, 1, 1, 1]
    assert b(data) == rel


def test_sorting():
    """Test sorting for various test cases."""
    print ('in test_sorting')
    assert b([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert b([1, 4, 3, 2]) == [1, 2, 3, 4]
    assert b([9, 9, 8, 9]) == [8, 9, 9, 9]
