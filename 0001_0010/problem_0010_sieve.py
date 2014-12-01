# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.  Find the sum of all the primes below two million.

primes = list([2,3,5,7])
result = 17

maxnum = 2000000

# populating the sieve of Eratosthenes - http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

sieve = set([2])

for i in range(1,maxnum/2+1):
    sieve.add(2*i)
for i in range(1,maxnum/3+1):
    sieve.add(3*i)
for i in range(1,maxnum/5+1):
    sieve.add(5*i)
for i in range(1,maxnum/7+1):
    sieve.add(7*i)

n = 9
while n < maxnum-2:
    n = n+2
    if n in sieve:
        continue
    else:
        primes.append(n)
        for k in range(1,maxnum/n+1):
                sieve.add(n*k)
        result = result + n
        print n

print result
# print sieve