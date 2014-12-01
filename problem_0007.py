# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  What is the 10001st prime number?

primes = list([2,3,5,7,11,13])

def next_prime(plist):
    length = len(plist)
    n = plist[length-1] + 2;
    found = 0
    while found != 1:
        for i in range(0,length):
            if plist[i]*plist[i] > n:
                found = 1
                break;
            if n%plist[i] == 0:
                break;
        if found == 1:
            return n
        n = n + 2

for i in range(7,10002):        
    n = next_prime(primes)
    primes.append(n)
    #print primes
    print i, n
    
# 10001 104743    