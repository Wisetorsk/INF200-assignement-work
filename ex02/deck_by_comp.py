# -*- coding: utf-8 -*-

"""
Compacting for loops using list comprehension
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    return [(suit, value) for suit in SUITS for value in VALUES]


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print "ERROR!"
