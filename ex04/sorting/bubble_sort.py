# -*- coding: utf-8 -*-

"""
source: INF200_H15_L03 lecture. H.E.Plesser
"""

__author__ = 'Marius Kristiansen'
__email__ = 'mariukri@nmbu.no'

def bubble_sort(data):
    sdata = list(data[:])

    for j in reversed(range(len(sdata))):
        for k in range(j):
            if not sdata[k] <= sdata[k+1]:
                sdata[k], sdata[k+1] = sdata[k+1], sdata[k]

    return sdata