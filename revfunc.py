#!/usr/bin/python

"""
reverse a string
"""

mystr = "this is my string"

def interative_reverse_string( str ):
    """ interative function to reverse a string """
    revstr = ''
    for i in xrange( len(str)-1, -1, -1 ):
        revstr = revstr + str[i]
    return revstr
    
print interative_reverse_string("this is my string")

