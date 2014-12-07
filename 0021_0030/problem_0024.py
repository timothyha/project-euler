# https://projecteuler.net/problem=24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# for n digits it's n! permutations
# 0, 1, ..., 8 has 9! = 362880
# 0, (1, ..., 9) -> 362880
# 1, (0, ..., 9) -> 362880
# 2, (0, ..., 9) -> 362880 - millionth is somewhere here, so we need to find 1000000 - 725760 = 274240

def fact(n):
    result = 1
    for i in range(1,n+1):
        result = i*result
    return result

def lex(lst, n, k):
    print n, "list", lst, "finding", k

    if n==1: return str(lst[0])
    if k==0:
        s = ""
        for i in range(0,n): s = s + str(lst[i])
        return s

    prev = fact(n-1)
    i = k/prev
    newlst = lst[:]
    elem = newlst.pop(i)
    return str(elem) + lex(newlst,n-1,k%prev)

if __name__ == '__main__':
    print lex([0,1,2,3,4,5,6,7,8,9], 10, 1000000)

"""
10 list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] finding 1000000
9 list [0, 1, 3, 4, 5, 6, 7, 8, 9] finding 274240
8 list [0, 1, 3, 4, 5, 6, 8, 9] finding 32320
7 list [0, 1, 3, 4, 5, 6, 9] finding 2080
6 list [0, 1, 4, 5, 6, 9] finding 640
5 list [0, 1, 4, 5, 6] finding 40
4 list [0, 4, 5, 6] finding 16
3 list [0, 4, 6] finding 4
2 list [0, 4] finding 0
2783915604
"""