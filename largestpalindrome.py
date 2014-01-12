#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

def is_palindrome (num):
	  palinstr = str(num)
	  palinlen = len(palinstr)
	  
	  for i in xrange(palinlen - 1):
		  if palinstr[i] != palinstr[palinlen - 1 - i]:
			  return 0
	  return 1

largest = 0
for i in xrange(999, 100, -1):
	for j in xrange(999, 100, -1):
		product = i * j
		if is_palindrome (product):
			print "found it %d X %d = %d" % ( i, j, product )
			if product > largest:
				largest = product
				largesti = i
				largestj = j

print largest
print largesti
print largestj
