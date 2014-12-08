# https://projecteuler.net/problem=48
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def powmod(n):
    result = n
    for i in range(1,n):
        result = (result * n) % 100000000000
    return result

if __name__ == '__main__':
    result = 405071317
    for n in range(11,1001):
        result = (result + powmod(n)) % 100000000000
        print n, result
    print result