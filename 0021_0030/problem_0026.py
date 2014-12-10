# https://projecteuler.net/problem=26 - Reciprocal cycles
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#    1/2	= 	0.5      1/3	= 	0.(3)     1/4	= 	0.25     1/5	= 	0.2     1/6	= 	0.1(6)     1/7	= 	0.(142857)
#     1/8	= 	0.125     1/9	= 	0.(1)     1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def ratio(k,n):
    digits = [k/n]
    moduli = []
    mod = 1
    while mod != 0:
        mod = (10*k) % n
        if mod in moduli: 
            return [digits, len(moduli)]
        moduli.append(mod)
        digits.append((10*k) / n)
        k = mod
    return [digits, 0]
    
#print ratio(1,4)
#print ratio(1,7)
#print ratio(1,10)
#print ratio(1,11)

if __name__ == '__main__':
    maxlen = 0
    maxnum = 0
    for i in range(1,1000):
        lst = ratio(1,i)
        if lst[1] > maxlen:
            maxlen = lst[1]
            maxnum = i
    print maxlen, maxnum