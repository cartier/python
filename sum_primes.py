#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


"""

def is_prime(num):
      if num < 2:
            return false

      for i in range(2,num-1):
            if num % i == 0:
                  return 0
      return 1

prime_sum = 0
for i in xrange(2, 2000000):
      if is_prime(i):
            prime_sum += i
            print "prime: %d" % i


print prime_sum
