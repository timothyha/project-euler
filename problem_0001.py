# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# learned something about Python sets
# we didn't use the fact that 3 and 5 have no common divisor and are prime numbers

def multiples_sum(limit, a, b):
	s = set([a,b]);
	if a*(limit/a) < limit:
		s.add(a*(limit/a));
	if b*(limit/b) < limit:
		s.add(b*(limit/b));
	for n in range(1,limit/a):
		s.add(n*a)
	for n in range(1,limit/b):
		s.add(n*b)
	
	result = 0
	for num in s:
		result = result + num
	return result
		
print multiples_sum(1000, 3, 5) # 233168
