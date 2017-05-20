# -*- coding: utf-8 -*-
"""
Created on Sat May 20 12:27:19 2017

@author: pnadolny
"""

def add_gigasecond(birth_date):
    from datetime import timedelta;
    gigadate = birth_date + timedelta(seconds = 1000000000)
    return gigadate;