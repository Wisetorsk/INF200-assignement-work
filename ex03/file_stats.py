# -*- coding: utf-8 -*-

"""
For some reason Pycharm detects a typo here, but i'm unable to find it.

The "Open(filename) call on line 18 can be inserted in place for the
variable "usr_file" if the file is run by itself or if it is possible
to add a "filename.close()" command within the list comp on line 19
 to compact it even more.
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def char_counts(filename):

    with open(filename, 'rb') as usr_file:  # Using "with" to reduce nu. lines
        bt_val = [ord(letter) for line in usr_file for letter in line]
        result = [bt_val.count(value) for value in range(265)]
    return result


if __name__ == '__main__':

    fname = 'file_stats.py'
    freqs = char_counts(fname)
    for code in range(256):
        if freqs[code] > 0:
            print('{:3}{:10}'.format(code, freqs[code]))
