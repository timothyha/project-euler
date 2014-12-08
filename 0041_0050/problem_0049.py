# https://projecteuler.net/problem=49
# The prime 41, can be written as the sum of six consecutive primes: 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# p1....pn - to check if pn lends new sum (in primes, < maxnum), we can go backwards from n to n-1 and get previous results

def stamp(n):
    s = sorted([n%10, ((n-n%10)%100)/10, ((n-n%100)%1000)/100, ((n-n%1000)%10000)/1000])
    result = ""
    for i in range(0,len(s)):
        result = result + str(s[i])
    return result

primes = [2]
stamps = [2]
maxnum = 10000

sieve = set([2])
for i in range(2,maxnum/2+1):
    sieve.add(2*i)

n = 3
while n <= maxnum:
    if n not in sieve:
        primes.append(n)
        stamps.append(stamp(n))
        for k in range(1,maxnum/n+1):
            sieve.add(n*k)
        #print n
    n = n+2 # loop further on odd numbers only

length = len(primes)
first = 0
for i in range(0,length):
    if primes[i] > 1000:
        first = i
        break
        
for n in range(first,length):
    stamp_n = stamp(n)
    for k in range(length-1,n,-1):
        if stamps[k] != stamps[n]: continue
        mid = (primes[k]+primes[n])/2
        if mid in primes:
            if stamps[primes.index(mid)] == stamps[k]:
                print "Found", primes[n], primes[primes.index(mid)], primes[k]

# Found 1487 4817 8147
# Found 2969 6299 9629                