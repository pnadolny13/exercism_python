# -*- coding: utf-8 -*-
"""
Created on Fri May 19 16:13:27 2017

@author: pnadolny
"""
pat = ['2017-01-05','2017-01-06asdfdf','2017-01-07asdf','2017-01-08exta','2017-01-09 extra','2017-01-10 pat']

def part(x):
    for i in x:
        x = x[:10];
    print (x);


part('2017-01-06asdfdf');

x = '2017-01-06asdfdf'
y = x[:10];
print(y);