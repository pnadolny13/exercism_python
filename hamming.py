# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 22:44:00 2017

@author: pnadolny
"""

def distance(x,y):
    count = 0;
    distance = 0;
    x = str.upper(x);
    y = str.upper(y);
    if len(x) != len(y):
        raise ValueError()
    if x.isalpha() and y.isalpha():
        for i in x:
            if i != y[count]:
                distance = distance +1;
            count = count +1;
    else:
        return False;
    return distance;
   