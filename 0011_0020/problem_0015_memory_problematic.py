# https://projecteuler.net/problem=15
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# We can grow trees from first node, adding neighbours on each step (water flowing down...) The numbers of ending nodes with coordinate of lower right corner will be the answer.

# first approach with storing of full routes cost much memory - see problem_0015_fullroutes.py
# better solution is to store only the end nodes, which are not [N,N] yet

# lists of (m,n) coordinates, which indicate some unfinished route, we start with 1,1
# coord = 100 x m + n to save memory
x = [101]
maxnum = 21 # square 20x20 has 21 nodes on each side
counter = 0

# THIS SOLUTION HAS A PROBLEM WITH MEMORY

i = 1
while i > 0:
    print "step", i, "===================================="
    finished = 1
    length = len(x)
    print "length", length, "counter", counter
    k = 0
    #print x
    #print y
    while k >= 0:
        xx = x[k]/100
        yy = x[k]%100
        if xx == maxnum and yy == maxnum:
            x.pop(k)
            counter = counter + 1
            if k >= len(x):
                break
            continue;
        # now extend route
        finished = 0
        if xx == maxnum: # we can go right only
            #print "right"
            x[k] = x[k]+1
        elif yy == maxnum: # we can go down only
            #print "down"
            x[k] = x[k]+100
        else: # we extend one route to the right and add one more route which goes down
            #print "right and down"
            x.append(x[k]+1)
            x[k] = x[k]+100
        k = k + 1
        if k >= len(x):
            break
    if finished == 1:
        break
    else:
        i = i+1

print "Answer:", counter
