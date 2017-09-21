# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:48:37 2017

@author: pnadolny
"""

def recursion(x):
    print (x)
    if x == 1:
        return 0;
    if x % 2 == 0:
        recursion(x/2);
    else:
        recursion(3*x+1);

recursion(10)
