# -*- coding: utf-8 -*-
import numpy as np

"""
I choose to use numpy's log functions, but I still use
Python's "sum()" for lists as I believe that is faster
I admit that the use of multiple "return"s is a bit clumsy.
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def entropy(message):

    bit_val = [ord(letter) for letter in message]
    if len(message) < 1:
        return 0
    else:
        p = [float(bit_val.count(value))/len(message) for value in bit_val]
        s = [(p[i]*np.log2(p[i])) for i in range(len(p))]
        s_entropy = - sum(s)
        if s_entropy == -0:
            return 0
        else:
            return s_entropy


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print "{:20}: {:10.3f} bits".format(msg, entropy(msg))
