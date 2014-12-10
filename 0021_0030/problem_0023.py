# https://projecteuler.net/problem=21
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be 
# expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# if we bring prime_layout function used earlier for primes numbers, d(n) will be faster to calculate, maybe

# if abd(n) = 1, will be abd(2n) = 1, abd(3n) = 1, etc.?

def d(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0: sum = sum + i
    return sum

def abd(n):
    if d(n) > n: return 1
    return 0

maxnum = 28123
abnums = []

for n in range(1,maxnum+1):
    if abd(n) == 1: 
        print n
        abnums.append(n)

length = len(abnums)

result = 0
for n in range(1,maxnum+1):
    found = 0
    for k in range(0,length):
        if abnums[k] > n/2: break
        if n-abnums[k] in abnums: 
            found = 1
            break
    if found == 0:
        result = result + n
        print n

print "Result", result 
"""
...
18437
19067
20161
Result 4179871
"""