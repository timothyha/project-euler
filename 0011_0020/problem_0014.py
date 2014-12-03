# https://projecteuler.net/problem=14
# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Wikipedia here: http://en.wikipedia.org/wiki/Collatz_conjecture
# check results here: http://oeis.org/A006877
# 1, 2, 3, 6, 7, 9, 18, 25, 27, 54, 73, 97, 129, 171, 231, 313, 327, 649, 703, 871, 1161, 2223, 2463, 2919, 3711, 6171, 10971, 13255, 17647, 23529, 26623, 34239, 35655, 52527, 77031, 106239, 142587, 156159, 216367, 230631, 410011, 511935, 626331, 837799

# we can save list of calculated n and resulting chains to save time
# we can also count quicker if we store only sizes
counted = [1,2,3,4]
sizes = [1,2,8,3]
maxsizes = [1,2,8,8]
maxnumbers = [1,2,3,3]

# 2 -> 1, 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1, 4 -> 2 -> 1

def collatz(n):
    if n == 1:
        return list([1])   
    result = list([n])
    if n % 2 == 0:
        result.extend(collatz(n/2))
    else:
        result.extend(collatz(3*n + 1))
    return result

def collatz_size(n):
    global sizes
    global counted
    
    if n in counted:
        #print "cache ", n
        return sizes[counted.index(n)]
    if n == 1:
        counted.append(1)
        sizes.append(1)
        return 1

    if n%2 == 0:
        return 1 + collatz_size(n/2)
    else:
        return 1 + collatz_size(3*n + 1)
    
    counted.append(n)
    sizes.append(result)
    return result    
    
# return max length and starting value in form of a list
def collatz_max(n):
    global sizes
    if n == 1:
        return list([1, 1])
    elif n == 2:
        return list([2, 2])
    elif n == 3:
        return list([3, 8])
    elif n == 4:
        return list([3, 8])

    if n <= len(maxnumbers):
        return list([maxnumbers[n-1], maxsizes[n-1]]);
        
    prevresult = collatz_max(n-1)
    maxnum = prevresult[0]
    maxlength = prevresult[1]
    
# N = 4K => 2K => K
# N = 4K + 1 => 12K + 4 => 6K + 2 => 3K + 1
# N = 4K + 2 => 2K + 1 => 6K + 4 => 3K + 2
# N = 4K + 3 => 12K + 10 => 6K + 5 => 18K + 16 => 9K + 8
    
    k = n/4
    m = n%4
    s = 0
    if m == 0:
        # we will go down into recursion only if there is a chance
        if maxsizes[k-1] + 2 > maxlength:
            s = 2 + collatz_size(k)
    elif m == 1:
        # 3*k+1 < 4*k+1
        if maxsizes[3*k+1-1] + 3 > maxlength:
            s = 3 + collatz_size(3*k+1)
    elif m == 2:
        # 3*k+2 < 4*k+2
        if maxsizes[3*k+2-1] + 3 > maxlength:
            s = 3 + collatz_size(3*k+2)
    else:
        # here we have to calculate with going up
        s = 4 + collatz_size(9*k+8)
        
    if s > maxlength:
        maxnum = n
        maxlength = s
        
    maxsizes.append(maxlength)
    maxnumbers.append(maxnum)
    return list([maxnum, maxlength])

print collatz(837799)    
    
for n in range(5,1000000):    
    print n, collatz_max(n)
# 837799    
print collatz(maxnumbers[999999])