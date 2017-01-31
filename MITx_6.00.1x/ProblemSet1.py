#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:00:18 2017

@author: lifanhong
"""

#problem set 1 (after the due date, cannot submit)

s = 'azcbobobegghakl'
#problem 1
count = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print('Number of vowels: ' + str(count))
#problem 2
count = 0
for i in range(len(s) - len('bob') + 1):
    if s[i:i + len('bob')] == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count))
#problem 3
