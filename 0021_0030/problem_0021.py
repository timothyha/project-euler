# https://projecteuler.net/problem=21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a <> b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def d(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0: sum = sum + i
    return sum

amicable = []

for n in range(1,10000):
    m = d(n)
    if m in amicable: continue;
    if m <> n:
        if d(m) == n:
            if m not in amicable: amicable.append(m)
            if n not in amicable: amicable.append(n)
            print m, n

print sum(k for k in amicable)

"""
284 220
1210 1184
2924 2620
5564 5020
6368 6232
31626
"""