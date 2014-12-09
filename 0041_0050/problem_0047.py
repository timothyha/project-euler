# https://projecteuler.net/problem=47
# The first two consecutive numbers to have two distinct prime factors are: 14 = 2 x 7 and 15 = 3 x 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2^2 x 7 x 23, 645 = 3 x 5 x 43, 646 = 2 x 17 x 19.
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

# populating list of primes, using problem 10's algorithm
primes = list([2])
maxnum = 10000000
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
        print n
    n = n+2 # loop further on odd numbers only

print "Primes count = ", len(primes)
    
saved_layouts = [[1],[2],[3],[2]];
    
def prime_layout(n):
    global primes
    global saved_layouts # to speed up things, we save intermediary results    
    
    if n == 1:
        return [1]

    if n <= len(saved_layouts):
        print "using cache for", n
        return saved_layouts[n-1]
        
    if n in primes:
        listprimes = [n]
        if len(saved_layouts) == n-1:
            #print "new prime", n
            saved_layouts.append(listprimes)
        return listprimes
    
    listprimes = []

    length = len(primes)
    for i in range(0,length):
        if primes[i] >= n:
            break;
        if n % primes[i] == 0:
            #print "recursion", n, primes[i], n/primes[i]
            sublist = prime_layout(n/primes[i])
            #print "sub", sublist
            listprimes = sublist[:]
            if primes[i] not in listprimes:
                #print listprimes, "add", primes[i]
                listprimes.append(primes[i])
            break
            
    if len(saved_layouts) == n-1:
        saved_layouts.append(listprimes)
    return listprimes

for n in range(2,13):
    print prime_layout(n)

n = 1
while n > 0:
    n = n + 1
    res = prime_layout(n)
    print n, res
    if len(res) != 4: continue
    res1 = prime_layout(n+1)
    if len(res1) != 4: 
        n = n + 1 # skip
        continue
    res2 = prime_layout(n+2)
    if len(res2) != 4: 
        n = n + 2 # skip
        continue
    res3 = prime_layout(n+3)
    if len(res3) != 4: 
        n = n + 3 # skip
        continue
    print "found", n, n+1, n+2, n+3
    break
# found 134043 134044 134045 134046