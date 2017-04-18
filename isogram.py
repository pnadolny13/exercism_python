# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 21:29:29 2017

@author: pnadolny
"""

def is_isogram(x):
    count = 0 ;
    letter_list = [];
    x = str.lower(x)
    for i in x:
        letter = x[count];
#new list if there is a space, not considered the same word
        if letter == " ":
            letter_list = [];
        if letter.isalpha():
            if letter in letter_list:
                return False;
                break;
        letter_list.append(x[count])
        count = count + 1;
    return True;
