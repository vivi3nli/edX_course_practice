# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
    global result
    #result = []
    for item in aList:
        if type(item) == list:
            #print(item)
            flatten(item)
        else:
            result += [item]
            #print("result", result)
    return result
'''


def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    result = []
    for item in aList:
        if type(item) != list:
            #print(item)
            result += [item]
        else:
            result += flatten(item)
            #print("result", result)
    return result

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))