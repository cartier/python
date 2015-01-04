#!/usr/bin/python
# -*- coding: utf-8 -*-

"""



By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def is_prime (num):
      for i in xrange(2, num):
            if num % i == 0:
                  return 0

      return 1


num_primes = 1


list = []
for i in xrange(1,1000):
      if is_prime (i):
            list.append(i)


product = 115189.0

#print list

for i in list:
      factor = product / i
      if(factor.is_integer()):
            if factor in list:
                  print("N37 59.{0} W084 33.{1}".format(i, int(factor)))
                  break
