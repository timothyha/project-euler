# https://projecteuler.net/problem=15
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# We can grow trees from first node, adding neighbours on each step (water flowing down...) The numbers of ending nodes with coordinate of lower right corner will be the answer.

# first approach with storing of full routes cost much memory - see problem_0015_fullroutes.py
# better solution is to store only the end nodes, which are not [N,N] yet

# lists of (m,n) coordinates, which indicate some unfinished route, we start with 1,1
# coord = 100 x m + n to save memory

maxnum = 21 # square 20x20 has 21 nodes on each side

cached = [maxnum * 100 + maxnum, maxnum * 100 + maxnum-1, maxnum * 100 + maxnum-100]
values = [0, 1, 1]

# how many routes to get from m x n to maxnum x maxnum
def routes(m,n):
    global cached
    global values

    if m == maxnum and n == maxnum:
        return 0
    elif m == maxnum:
        return 1
    elif n == maxnum:
        return 1
    
    if (m*100 + n) in cached:
        return values[cached.index(m*100+n)]
    
    result = routes(m+1, n) + routes(n+1, m) #- routes(m+1, n+1)
    cached.append(m*100 + n)
    values.append(result)    
    return result
    
for i in range(maxnum, 0, -1):
    for k in range(maxnum, 0, -1):
        print i, k, routes(i,k)

#1 1 137846528820