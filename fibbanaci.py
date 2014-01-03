#!/usr/bin/python


"""

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

next_fib = 0
fibanacci_sequence = [ 1 ,2 ]

fib_sum = 0

i = 2
while 1:
	next_fib = fibanacci_sequence [i - 1] + fibanacci_sequence [i - 2]  
	if next_fib > 4000000:
		break;
	fibanacci_sequence.append(next_fib)
	i += 1
	print next_fib
	if next_fib % 2 == 0:
		fib_sum += next_fib

print fibanacci_sequence

sum=0
for f in fibanacci_sequence:
	if f % 2 == 0:
		print f
		sum += f

print sum

print fib_sum
