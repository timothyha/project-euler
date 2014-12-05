# https://projecteuler.net/problem=16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# Check also http://en.wikipedia.org/wiki/Digit_sum for mathematical formula

# Here we calculate ALL digits

digits = [1]

for n in range(1,1001):
    # multiple by 2
    length = len(digits)
    
    k = 0
    carry = 0
    while k < length-1:
        digits[k] = digits[k] + digits[k] + carry
        if digits[k] >= 10:
            digits[k] = digits[k] % 10
            carry = 1
        else:
            carry = 0
        k = k+1
            
    digits[length-1] = digits[length-1] + digits[length-1] + carry
    if digits[length-1] >= 10:
        digits.append(digits[length-1]/10)
        digits[length-1] = digits[length-1]%10

    print "2 pow", n, "sum of digits", sum(n for n in digits) #, digits[len(digits)-1]
    
#2 pow 999 sum of digits 1367
#2 pow 1000 sum of digits 1366