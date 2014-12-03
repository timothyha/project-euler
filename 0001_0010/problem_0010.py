# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.  Find the sum of all the primes below two million.

primes = list([2])
result = 2

maxnum = 2000000

# populating the sieve of Eratosthenes - http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

sieve = set([2])

for i in range(2,maxnum/2+1):
    sieve.add(2*i)

n = 3
while n <= maxnum:
    if n not in sieve:
        primes.append(n)
        for k in range(1,maxnum/n+1):
            sieve.add(n*k)
        result = result + n
        print n

    n = n+2 # loop further on odd numbers only

print result # 142913828922
# print sieve