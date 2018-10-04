# -*- coding: utf-8 -*-

"""
source: INF200_H15_L04 lecture. H.E.Plesser
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'

def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data
    """
    if data == []:
        raise ValueError('Given list is empty')
    else:
        sdata = sorted(data)
        n = len(sdata)
        return (sdata[n / 2] if n % 2 == 1
                else 0.5 * (sdata[n / 2 - 1] + sdata[n / 2]))
