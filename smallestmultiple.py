#!/usr/bin/python
# -*- coding: utf-8 -*-

"""



2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

num = 20
## while 1:
## 	is_divisible = 1
## 	for i in xrange(1,21):
## 		if num % i != 0:
## 			is_divisible = 0
## 			break
## 	if is_divisible:
## 		print num
## 		break
## 	num += 1
## 	if num % 1000000 == 0:
## 		print num


def prime_factorization (num):
	""" return a list of prime factors for a number """
	primelist = []

	primedict = {}
	while 1:
		for i in xrange(2, num + 1):
			if num % i == 0:
				primelist.append(i)
				if i in primedict:
					primedict[i] += 1
				else:
					primedict[i] = 1

				num = num / i
#				primedict[0] += 1
				break
		if num == 1:
			break
#	print primedict[0] # number of factors
	return primedict

#print prime_factorization (2520)

def merge_factors (current_prime_dict, dict_to_merge):
	"""
	merge dict_to_merge into current_dict with no duplication

	one way to do it is to keep an array of count for each factor 

	"""

	for key in dict_to_merge:
		value = dict_to_merge[key]
		if key in current_prime_dict:
			if value > current_prime_dict[key]:
				current_prime_dict[key] = value
		else:
				current_prime_dict[key] = value

	return current_prime_dict


#print prime_factorization(20)

prime_dict = {}
for i in range(2, 21):
	tmp_dict = prime_factorization(i)
#	print tmp_dict
	prime_dict = merge_factors (prime_dict, prime_factorization(i))

print prime_dict
print len(prime_dict)

product = 1
for key in prime_dict:
	product *= pow(key, prime_dict[key])

print product



