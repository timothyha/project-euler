# https://projecteuler.net/problem=49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

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
        mid = (primes[k]+primes[n])/2 # arithmetic sequence!
        if mid in primes:
            if stamps[primes.index(mid)] == stamps[k]:
                print "Found", primes[n], primes[primes.index(mid)], primes[k]

# Found 1487 4817 8147
# Found 2969 6299 9629                