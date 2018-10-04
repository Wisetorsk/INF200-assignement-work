# -*- coding: utf-8 -*-

import random as rng

"""
Program simulating walking home in one dimention
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


class Walk(object):

    def __init__(self, home, start=0):
        """
        Constructor
        - The "start" parameter can be altered, but will essestially be same as
        altering home with the same amount.
        :param home:
        :param start:
        :return:
        """
        self._home = home
        self._position = start
        self._steps = 0
        self._steplist = []

    def direction(self):
        """
        Determines the direction the program will take the next step in.

        :return:
        """
        way = rng.randint(1, 2)
        if way == 1:
            self._position -= 1
        else:
            self._position += 1
        self._steps += 1

    @property
    def am_i_home(self):
        """
        Tests if the current position in the same as the "home"-coordinate

        :return:
        """
        if self._position == self._home:
            self._steplist.append(self._steps)
            return True

    def position(self):
        """
        Query the program for the current position

        :return:
        """
        return self._position

    def walking_home(self):
        """
        Runs the step method (direction()) n
        times and checks if the program is "home"
        Also resets _steps and _position to prepare for next program execution

        :return:
        """
        while True:
            self.direction()
            if self.am_i_home is True:
                self._steps = 0
                self._position = 0
                break

    def simulate(self, n):
        """
        Runs the simulation the number of times specified.
        - Distance to home is the same
        - Only number of times the single simulation is run can be altered here

        :param n:
        :return:
        """
        for _ in range(n):
            self.walking_home()
        print "Distance: {:4} -> Path Length: {}".\
            format(self._home, self._steplist)


if __name__ == '__main__':
    distances = [Walk(dist) for dist in [1, 2, 5, 10, 20, 50, 100]]
    # rng.seed(265)
    for d in distances:
        d.simulate(5)
