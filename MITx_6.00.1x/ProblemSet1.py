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
l_len = 0 #longest length
l_str = '' #longest string
for i in range(len(s)):
    c_str = s[i] #current string, initialize to every new char
    c_len = 1 #current string length
    if (len(s) - i - 1) <= l_len:
        break
    else: 
        for c in range(i,len(s) - 1):
            if s[c + 1] >= s[c]:
                c_str += s[c + 1]
                c_len += 1
            else:
                break
    if c_len > l_len:
        l_str = c_str
        l_len = c_len

print("Longest substring in alphabetical order is: " + l_str)

#All above have passed the online grader