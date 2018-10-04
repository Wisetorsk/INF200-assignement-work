# -*- coding: utf-8 -*-

"""
Small script that counts letters in a sentence.
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def letter_freq(txt):
    frequency = {}
    for ltr in txt.lower():
        if ltr in freqs:
            frequency[ltr] += 1
        else:
            frequency[ltr] = 1
    return freqs

if __name__ == '__main__':
    text = raw_input('Please enter text to analyse: ')
    freqs = letter_freq(text)
    for letter, count in sorted(freqs.items()):
        print('{:3}{:10}'.format(letter, count))
