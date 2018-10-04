# -*- coding: utf-8 -*-

"""
Two types of Number generators.
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class LCGRand(object):
    """
    Pseudo-Random Number Generator (Prng)
    using LCG-algorithm to generate numbers
    """

    def __init__(self, seed):
        """
        Constructor

        :param seed:
        :return:
        """
        self._seed = seed

    def rand(self):
        """
        Updates the "_seed" value and returns it to the user

        :return self._seed:
        """
        self._seed = (7**5 * self._seed) % ((2**31)-1)
        return self._seed


class ListRand(object):
    """
    "Random" number generator using a pre-determined list of numbers as source
    """
    def __init__(self, numbers):
        """
        Constructor

        :param numbers:
        :return:
        """
        self._numbers = numbers

    def rand(self):
        """
        Returns the first element in the list, but does so destructively

        :return self._numbers.pop(0):
        """
        if len(self._numbers) == 0:
            raise RuntimeError('Given list has run out of numbers!')
        else:
            return self._numbers.pop(0)


if __name__ == '__main__':
    RNG_1 = LCGRand(1234)  # Seed value, change for updated output
    RNG_2 = ListRand([1, 75, 3, 8, 345, 478, 2546, 7486, 453, 23123, 99678])
    print '\n\nNumbers generated using LCG algorithm based PseudoRNG:'
    for _ in range(10):
        print RNG_1.rand()
    print '\n\n'
    print 'Numbers "generated" using ListRand:'
    for _ in range(10):
        print RNG_2.rand()
