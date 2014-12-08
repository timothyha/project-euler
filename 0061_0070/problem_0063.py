# https://projecteuler.net/problem=63
# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

"""
a^n > 10^(n-1)
n log a > (n-1)
1 + 1/(n-1) > 1 / log 9
n <= 22
Just check all n-th power until 22-th
"""

# a, b are lists
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

# a is a list, n is integer
def digit_pow(a,n):
    if a==1: return [1]

    aval = a[-1]
    for i in range(len(a)-2,-1,-1):
        aval = 10 * aval + a[i]

    result = a[:]
    for k in range(0,n-1):
        c = result[:]
        # multiply by a
        for i in range(0,aval-1):
            result = digit_sum(c,result)
            #print result
    return result

if __name__ == '__main__':
    found = []

    for dig in range(1,10):
        for n in range(1,23):
            newlist = digit_pow([dig],n)
            if len(newlist) == n:
                if newlist not in found:
                    found.append(newlist)
                print newlist, dig, "pow", n

    print "result", len(found) # result 49

"""
[1] 1 pow 1
[2] 2 pow 1
[3] 3 pow 1
[4] 4 pow 1
[6, 1] 4 pow 2
[5] 5 pow 1
[5, 2] 5 pow 2
[5, 2, 1] 5 pow 3
[6] 6 pow 1
[6, 3] 6 pow 2
[6, 1, 2] 6 pow 3
[6, 9, 2, 1] 6 pow 4
[7] 7 pow 1
[9, 4] 7 pow 2
[3, 4, 3] 7 pow 3
[1, 0, 4, 2] 7 pow 4
[7, 0, 8, 6, 1] 7 pow 5
[9, 4, 6, 7, 1, 1] 7 pow 6
[8] 8 pow 1
[4, 6] 8 pow 2
[2, 1, 5] 8 pow 3
[6, 9, 0, 4] 8 pow 4
[8, 6, 7, 2, 3] 8 pow 5
[4, 4, 1, 2, 6, 2] 8 pow 6
[2, 5, 1, 7, 9, 0, 2] 8 pow 7
[6, 1, 2, 7, 7, 7, 6, 1] 8 pow 8
[8, 2, 7, 7, 1, 2, 4, 3, 1] 8 pow 9
[4, 2, 8, 1, 4, 7, 3, 7, 0, 1] 8 pow 10
[9] 9 pow 1
[1, 8] 9 pow 2
[9, 2, 7] 9 pow 3
[1, 6, 5, 6] 9 pow 4
[9, 4, 0, 9, 5] 9 pow 5
[1, 4, 4, 1, 3, 5] 9 pow 6
[9, 6, 9, 2, 8, 7, 4] 9 pow 7
[1, 2, 7, 6, 4, 0, 3, 4] 9 pow 8
[9, 8, 4, 0, 2, 4, 7, 8, 3] 9 pow 9
[1, 0, 4, 4, 8, 7, 6, 8, 4, 3] 9 pow 10
[9, 0, 6, 9, 5, 0, 1, 8, 3, 1, 3] 9 pow 11
[1, 8, 4, 6, 3, 5, 9, 2, 4, 2, 8, 2] 9 pow 12
[9, 2, 3, 8, 2, 8, 5, 6, 8, 1, 4, 5, 2] 9 pow 13
[1, 6, 9, 4, 5, 4, 2, 9, 7, 6, 7, 8, 2, 2] 9 pow 14
[9, 4, 6, 4, 9, 0, 2, 3, 1, 1, 9, 8, 5, 0, 2] 9 pow 15
[1, 4, 8, 1, 5, 8, 8, 8, 1, 0, 2, 0, 3, 5, 8, 1] 9 pow 16
[9, 6, 5, 6, 6, 6, 9, 9, 6, 1, 8, 1, 7, 7, 6, 6, 1] 9 pow 17
[1, 2, 1, 9, 9, 9, 6, 9, 2, 5, 3, 6, 4, 9, 0, 0, 5, 1] 9 pow 18
[9, 8, 0, 2, 9, 9, 2, 7, 6, 7, 1, 7, 1, 5, 8, 0, 5, 3, 1] 9 pow 19
[1, 0, 8, 8, 2, 9, 6, 5, 0, 9, 5, 4, 5, 6, 6, 7, 5, 1, 2, 1] 9 pow 20
[9, 0, 2, 9, 5, 3, 2, 1, 5, 1, 3, 1, 9, 8, 9, 8, 1, 4, 9, 0, 1] 9 pow 21
"""