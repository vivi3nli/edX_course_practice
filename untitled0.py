#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 00:30:48 2017

@author: lifanhong
"""
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
    
"""

print("hello world")

if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    print('smaller')
    
n = 2
while n <= 10:
    print(n)
    n += 2
print('Goodbye!')

print('Hello!')
n = 10
while n >= 2:
    print(n)
    n -= 2

n = 1
end = 6
sum = 0
while n <= end:
    sum += n
    n += 1
print(sum)

for n in range(2,11,2):
    print(n)
print('Goodbye!')

print('Hello!')
for n in range(10,1,-2):
    print(n)
    
sum = 0
for n in range(1,7):
    sum += n
print(sum)