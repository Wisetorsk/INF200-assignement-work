# -*- coding: utf-8 -*-
from random import randint as rng
"""
Tidying up and clarifying code
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def query_user():
    usr_guess = 0
    while usr_guess < 1:
        usr_guess = int(raw_input('Your guess: '))
    return usr_guess


def rng_integer_sum():
    return rng(1, 6) + rng(1, 6)


def value_test(value_1, value_2):
    return value_1 == value_2


if __name__ == '__main__':
    outcome = False
    points = 3
    answer = rng_integer_sum()
    while not outcome and points > 0:
        guess = query_user()
        h = value_test(answer, guess)
        if not outcome:
            print('Wrong, try again!')
            points -= 1

    if points > 0:
        print('You won {} points.'.format(points))
    else:
        print('You lost. Correct answer: {}.'.format(answer))
