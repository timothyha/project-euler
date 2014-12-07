# https://projecteuler.net/problem=50
# The prime 41, can be written as the sum of six consecutive primes: 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# p1....pn - to check if pn lends new sum (in primes, < maxnum), we can go backwards from n to n-1 and get previous results

primes = list([2])
maxnum = 1000000

sieve = set([2])
for i in range(2,maxnum/2+1):
    sieve.add(2*i)

n = 3
while n <= maxnum:
    if n not in sieve:
        primes.append(n)
        for k in range(1,maxnum/n+1):
            sieve.add(n*k)
        print n
    n = n+2 # loop further on odd numbers only

memolist = []
memosum = []
# sum of primes from i-th to k-th
def memoize(i,k):
    ind = str(i) + "-" + str(k) 
    if ind in memolist:
        #print "cache", ind
        return memosum[memolist.index(ind)]
    if k == i:
        return primes[i-1]
    else:
        result = memoize(i,k-1) + primes[k-1]

    memolist.append(ind)
    memosum.append(result)
    return result

# 2, 3, 5, 7 ...
# N = 1, MAX = 1
# N = 2, MAX = 1
# N = 3, MAX = 2 (2+3 = 5)
# N = 4, MAX = 2

maxlengths = list([1, 2, 2, 2])
maxprimes = list([2, 2, 5, 5])

length = len(primes)
print "number of primes:", length

for n in range(5,length):
    notfound = 1
    maxlengths.append(maxlengths[n-2])
    maxprimes.append(maxprimes[n-2])

    # test at least same length
    for k in range(n-maxlengths[n-1]+1,-1,-1):
        sum = memoize(k,n)
        if sum > maxnum:
            break
        elif sum in primes:
            if n-k+1 > maxlengths[n-1]:
                notfound = 0
                print sum, "length", n-k+1, "from", k, "to", n
                maxlengths[n-1] = n-k+1
                maxprimes[n-1] = sum

# 997651 length 543 from 4 to 546
