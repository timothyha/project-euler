# https://projecteuler.net/problem=2
# The prime factors of 13195 are 5, 7, 13 and 29.  What is the largest prime factor of the number 600851475143 ?

import math

primes = list([2,3,5,7])
limit = 87625999 # 600851475143

lim = int(math.ceil(math.sqrt(limit)));
maxp = 1

# first loop to check current primes
for n in primes:
    if limit%n == 0:
        maxp = n

# second loop to get all primes into set
for n in range(8, lim):
    notprime = 0
    for p in primes:
        if p*p > n:
            break
        elif n%p == 0:
            notprime = 1
            break
    if notprime == 0:
        primes.append(n)
        if limit%n == 0:
            maxp = n

#print primes # ... 524269, 262127, 524273, 727997, 262133, 618361, 567977, 524281, 262139, 715781, 698323, 524287])
print maxp # 600851475143 -> 6857