# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime

class Person(object):
    def __init__(self, name):
        """
        create a person called name
        """
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        return self.lastName
        
    def setBirthday(self, month, day, year):
        """
        set self's birthday to birthDate
        """
        
    def __str__(self):
        """
        return self's name
        
        It's overriding the built-in __str__ so that
        when we want to print out something, this 
        method will be print out
        """
        return self.name
        
        
class MITPerson(Person)