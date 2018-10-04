# -*- coding: utf-8 -*-

"""
Expanding list comprehension into a conventional "for loop" -form
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def squares_by_comp(number):
    return [k**2 for k in range(number) if k % 3 == 1]


def squares_by_loop(n):
    squares = []
    for number in range(n):
        if number % 3 == 1:
            squares.append(number**2)
    return squares

if __name__ == '__main__':
    number_in = int(raw_input('Number: '))
    if squares_by_comp(number_in) != squares_by_loop(number_in):
        print 'ERROR!'
