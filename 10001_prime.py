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

factor = 2
while num_primes < 10001:
      factor += 1
      if is_prime(factor):
            num_primes += 1


print num_primes
print factor

