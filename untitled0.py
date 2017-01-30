#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 00:30:48 2017

@author: lifanhong
"""

print('hello world')
print('I like 6.00.1x')
#in the following 3 expreesions, the word[-1]
#repersents the last char of the string and
#when the gap is -1 it starts at word[-1]

print('')
print('abcdefgh'[::-1])
print('abcdefgh'[:-1:-1])
print('abcdefgh'[:-1])
print('abcdefgh'[:-2:-1])

x = 6
if x != 5:
    print('haha')
else:
    print('kiki')

#我的小错题集

num = 10
for num in range(5):
    print(num)
print(num)

#output 0, 1, 2, 3, 4, 4

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 

#output 0.0, 1.0, 2.0, 3.0, 4.0

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 

#output 0, 'Foo!', 4, 8, 12, 16, 'Foo!'

