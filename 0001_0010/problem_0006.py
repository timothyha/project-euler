# https://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sq_of_sum(n):
    s = (n*(n+1))/2
    return s*s
    
def sum_of_sq(n):
    s = 1
    for i in range(2,n+1):
        s = s + i*i
    return s
    
print sq_of_sum(100) - sum_of_sq(100)