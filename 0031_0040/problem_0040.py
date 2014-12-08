# https://projecteuler.net/problem=40
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

"""
This could help:
1-9 - 9 x 1 digits
10-99 - 91 x 2 digits
100-999 - 901 x 3 digits
1000-9999 - 9001 x 4 digits, etc.
"""

"""
Somewhat slower solution below
"""
digits = [1]
length = 1
prevlength = 1
d = [1] # d(1) here

queue = [10,100,1000,10000,100000,1000000] # queue of expected n-th digits

"""
We will gradually add numbers to the line, which starts with 1 (1, 12, 123, ...) until there are enough digits
"""
while len(queue) > 0:
    while length < queue[0]:
        # add one more number
        carry = (digits[0] + 1)/10
        digits[0] = (digits[0] + 1)%10
        for i in range(1,len(digits)):
            s = digits[i] + carry
            carry = s/10
            digits[i] = s%10
        if carry > 0:
            digits.append(1)
        
        prevlength = length
        length = length + len(digits)
        print digits, length, queue[0]
        
    i = queue[0]-prevlength
    d.append(digits[len(digits)-i]) # digits are stored in reversed order
    queue.pop(0)
    
print d
    
    