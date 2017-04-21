# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 22:42:11 2017

@author: pnadolny
"""

def to_rna(dna):
    dna = str.upper(dna);
    rna = [];
    for i in dna:
        if i == "G":
            rna.append("C");
        elif i == "C":
            rna.append("G");
        elif i == "T":
            rna.append("A");
        elif i == "A":
            rna.append("U");
        else:
            rna = [];
            break;
    rna = ''.join(rna);
    return rna;