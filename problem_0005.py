# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def common_div(a,b): # find common divisible by going up from a to a*b, if a > b it's the shorter way
    for i in range(1,b):
        if i*a%b == 0:
            return i*a
    return a*b

start = 1
for i in range(2,101):
    newstart = common_div(start,i);
    print i, newstart
    start = newstart
    
# 20 232792560    