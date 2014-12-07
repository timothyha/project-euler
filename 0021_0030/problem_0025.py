# https://projecteuler.net/problem=20
# The Fibonacci sequence is defined by the recurrence relation: Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1 F2 = 1 F3 = 2 F4 = 3 F5 = 5 F6 = 8 F7 = 13 F8 = 21 F9 = 34 F10 = 55 F11 = 89 F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the first term in the Fibonacci sequence to contain 1000 digits?

# a < b
def digit_sum(a,b):
    c = []
    carry = 0
    for i in range(0,len(a)):
        s = a[i]+b[i]+carry
        carry = s/10
        c.append(s%10)
    for i in range(len(a),len(b)):
        s = b[i]+carry
        carry = s/10
        c.append(s%10)
    if carry > 0:
        c.append(carry)
    return c

if __name__ == '__main__':
    # F11 = 89 F12 = 144
    a = [9,8]
    b = [4,4,1]
    n = 12
    while n > 0:
        n = n+1
        print n
        c = digit_sum(a,b)
        if len(c)>=1000:
            print "Found"
            break
        a = b[:]
        b = c[:]
        