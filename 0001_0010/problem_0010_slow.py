# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.  Find the sum of all the primes below two million.

# some mathematical reasoning: each next prime number P is the first number which cannot be divided by any of the previously calculated prime numbers which are >=2 and <=square root of P

# reusing some code from problem 7

primes = list([2,3,5,7,11,13])
length = 6
result = 41
n = 13
maxnum = 2000000

# checking by n = n+2 is really slow, but there are many pairs of prime numbers in form of (n, n+2)
# could it be faster if I populate a bitmap of non-prime numbers?
# current solution is too slow, about 10 minutes of runtime
# look at the other script "problem_0010_sieve.py"

while n < maxnum:         
    n = primes[length-1] + 2;
    found = 0
    while found != 1: # searching for next prime number
        for i in range(0,length):
            if primes[i] * primes[i] > n:
                found = 1
                break;
            if n % primes[i] == 0:
                break;
        if found == 1:
            print n
            primes.append(n)
            length = length + 1
            result = result + n
        n = n+2
        if n >= maxnum:
            break

print result # 142913828922

# 1999859
# 1999867
# 1999871
# 1999889
# 1999891
# 1999957
# 1999969
# 1999979
# 1999993