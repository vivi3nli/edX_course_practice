#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:25:52 2017

@author: lifanhong
"""
#Exercise: guess my number
print("Please think of a number between 0 and 100!")
guess = 50
high = 100
low = 0
status = ''
while True:
    print("Is your secret number " + str(guess) + "?")
    status = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if status == 'h':
        high = guess
        guess = (high + low) // 2
    elif status == 'l':
        low = guess
        guess = (high + low) // 2 #the guess should be int
    elif status == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(guess))

