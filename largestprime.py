#!/usr/bin/python


"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import math


num = 600851475143


def testprime(num):
    for i in range(2,num-1):
        if num % i == 0:
            return 0
    return 1


startfactor = int(math.sqrt(num))
print startfactor 


for factor in range (startfactor, 1, -1):
    if num % factor == 0:
        print factor
        if testprime(factor):
            print "This is the one : %d!" % factor


