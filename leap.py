# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:20:13 2017

@author: pnadolny
"""
def is_leap_year(x):
    x = int(x)
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
        else:
            return True
    else:
        return False