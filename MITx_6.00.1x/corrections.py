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
#即使预先赋值了num，依然可以进入for loop

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor) 

#output 0.0, 1.0, 2.0, 3.0, 4.0
#a/b = float, a//b = int

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 

#output 0, 'Foo!', 4, 8, 12, 16, 'Foo!'
#0 % 16 == 0

#a surprisingly simple piece of code to solve Hanoi Problem
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))

#Exercise: is in
#bisection search to determine if a character is in a string, so long
#as the string is sorted in alphabetical order

def isIn(char, aStr):
   '''
   char: a single character
   aStr: an alphabetized string
   
   returns: True if char is in aStr; False otherwise
   '''
   # Base case: If aStr is empty, we did not find the char.
   if aStr == '':
      return False

   # Base case: if aStr is of length 1, just see if the chars are equal
   if len(aStr) == 1:
      return aStr == char

   # Base case: See if the character in the middle of aStr equals the 
   #   test character 
   midIndex = len(aStr)//2
   midChar = aStr[midIndex]
   if char == midChar:
      # We found the character!
      return True
   
   # Recursive case: If the test character is smaller than the middle 
   #  character, recursively search on the first half of aStr
   elif char < midChar:
      return isIn(char, aStr[:midIndex])

   # Otherwise the test character is larger than the middle character,
   #  so recursively search on the last half of aStr
   else:
      return isIn(char, aStr[midIndex+1:])


