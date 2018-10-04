# -*- coding: utf-8 -*-

"""
If there is a way to include multiple line statements inside a
list comprehension it could drastically reduce the number of lines needed
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'


def bubble_sort(data_list):

    output = list(data_list)
    if len(data_list) == 0 or len(data_list) == 1:
            pass  # Returns a empty list
    else:
        for n in range(len(output)):
            for index in range(1, len(output)):
                if output[index-1] > output[index]:
                    temp = output[index]
                    output[index] = output[index-1]
                    output[index-1] = temp
    return tuple(output)


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print "{:30} --> {:30}".format(data, bubble_sort(data))
