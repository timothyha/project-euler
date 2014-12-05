# https://projecteuler.net/problem=16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# Check also http://en.wikipedia.org/wiki/Digit_sum for mathematical formula

# Here we calculate ALL digits using map and reduce stuff

digits = [1]

def add(x,y): return x+y

for n in range(1,1001):
    # multiple by 2
    length = len(digits)
    doubles = [ digits[i]+digits[i] for i in range(0, length) ]
    #print doubles
    k = 0
    while k < length-1:
        if doubles[k] >= 10:
            digits[k] = doubles[k] % 10
            doubles[k+1] = doubles[k+1]+1
        else:
            digits[k] = doubles[k]
        k = k+1
            
    if doubles[length-1] >= 10:
        digits[length-1] = doubles[length-1]%10
        digits.append(doubles[length-1]/10)
    else:
        digits[length-1] = doubles[length-1]

    print "2 pow", n, "sum of digits", reduce(add, digits), digits[length-1]
    
#2 pow 999 sum of digits 1367 5
#2 pow 1000 sum of digits 1366 0