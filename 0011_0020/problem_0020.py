# https://projecteuler.net/problem=20
# n! means n x (n - 1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

digits = [1]

for n in range(2,101):
    length = len(digits)   
    k = 0
    carry = 0
    while k < length-1:
        digits[k] = digits[k] * n + carry
        if digits[k] >= 10:
            carry = digits[k] / 10
            digits[k] = digits[k] % 10
        else:
            carry = 0
        k = k+1
            
    digits[length-1] = digits[length-1] * n + carry
    while digits[length-1] >= 10:
        digits.append(digits[length-1]/10)
        digits[length-1] = digits[length-1]%10
        length = length + 1

    print "Factorial", n, "sum of digits", sum(a for a in digits)
