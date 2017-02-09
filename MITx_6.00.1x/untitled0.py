#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 00:30:48 2017

@author: lifanhong
"""

def gene(dad, mom):
    """
    to modify the gene passing of creatures
    the input is the locus 
    """
    for a in dad:
        for b in mom:
            print(a + b)

            
gene('','')
print()

#when it's exceeding 2 genes the output is 2 which is not right

#wanna go to sleep earlier today, maybe not commiting 
