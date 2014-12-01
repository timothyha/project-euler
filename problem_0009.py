# https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# a < b < c => a < 333
# b + c < 1000 => b < 500

for a in range(1,333):
    aa = a*a # to save time for calculations in loop
    for b in range(a+1,500):
        bb = b*b
        c = 1000-a-b
        if c<=b: 
            continue
        else:
            if c*c == aa+bb:
                print a*b*c, a, b, c # 31875000 200 375 425