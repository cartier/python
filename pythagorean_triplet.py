#!/usr/bin/python
# -*- coding: utf-8 -*-

"""



A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


"""


def calc_a(b):
      a = (1000000 - 2000 * b) / (2000.0 - 2 * b)
      return a

def is_int(val):
      if val - int(val) == 0:
            return 1
      else:
            return 0


for b in xrange(1000):
      try_a = calc_a(b)
      if is_int(try_a):
            c = 1000 - try_a - b
            if try_a < 0 or try_a >= b or b >= c:
                  continue
            print "found it"
            print try_a, b, c
            print int(try_a * b * c)





