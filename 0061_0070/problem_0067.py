# https://projecteuler.net/problem=18
"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
"""

# Algorithm for problem 18 and 67:
# If numbers on last row are different (at least for neighbours), then we can choose as following
# 1) for each neighbouring pair A < B (or B > A) with C on top we can decide that route C-A is impossible. Otherwise it could be replaced by C-B with a larger sum
# 2) we replace C with value of C+B (future value) and similarly do this with all items on row previous to last row
# 3) repeat same steps until we get to last two rows on top, there we can choose, and find our way back to get the path

lines = [line.strip() for line in open('p067_triangle.txt')]

row = []
for n in range(0, len(lines)):
    row.append([int(i) for i in lines[n].split()])

print row[0]
print row[1]
print row[len(row)-1]

for n in range(len(row)-1,0,-1):
    print n
    for k in range(0, n):
        if row[n][k] < row[n][k+1]:
            row[n-1][k] = row[n-1][k] + row[n][k+1]
        else:
            row[n-1][k] = row[n-1][k] + row[n][k]
    print row[n-1]

print row[0][0];
