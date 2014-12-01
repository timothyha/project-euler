# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 ? 99. Find the largest palindrome made from the product of two 3-digit numbers.

def palindromic(n):
    s = str(n)
    length = len(s)
    for i in range(0,length/2+1):
        if s[i] != s[length-i-1]:
            return 0
    return 1
   
max = 10201 # 101 * 101
maxi = 101
maxj = 101

for i in range(100,1000):
    for j in range(i,1000):
        if palindromic(i*j):
            if i*j > max:
                max = i*j
                maxi = i
                maxj = j

print maxi, maxj, max # 913 993 906609