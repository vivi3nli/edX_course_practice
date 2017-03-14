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
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """
        returns self's current age in days
        """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    def __lt__(self, other):
        """
        return True if self's name is lexicographically
        less than other's name, and False otherwise
        """
        if self.lastName == other.name:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """
        return self's name
        
        It's overriding the built-in __str__ so that
        when we want to print out something, this 
        method will be print out
        """
        return self.name
        
        
class MITPerson(Person):
    """
    nextIdNum is a data attributes that's built in to
    the class, not belonging to any instance but belongs 
    to the class
    """
    nextIdNum = 0 # next ID number to assign
    
    def __init__(self, name):
        Person.__init__(self, name) #initialize Person attribute
        self.idNum = MITPerson.nextIdNum #MITPerson attribute: unique ID
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
    """
    sort MIT people use their ID number, not name
    
    eg:
        p1 < p2
        will be converted into p1.__lt__(p2)
        thus if p2 isn't a MITPerson there'll be an error
    """
        return self.idNum < other.idNum
    
    def speak(self, utterance):
    """
    returns a string that can be printed
    
    every child class inherited the methods of parent class,
    while parent class cannot reach child class
    """
        return (self.getLastName() + " says:" + utterance)