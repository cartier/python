#!/usr/bin/python

"""
reverse a string
"""

mystr = "this is my string"



print mystr
print mystr[::-1]


mylen = len(mystr)

myrevstr = ''
for i in xrange(len(mystr) - 1, -1, -1):
#	print mystr[i]
	myrevstr += mystr[i]

print "Iterative reversal: " + myrevstr



def revstr(str) :
	""" recursive function to reverse a string """

	str_len = len(str)
	if str_len == 1 :
		return str

	new = str[str_len-1] + revstr(str[:str_len-1])
	return new
	




print "Recursive string function doc string" + revstr.__doc__
print "Recursive string function doc string" + revstr(revstr.__doc__)

print "Recursive reversal: "+ revstr(mystr)
