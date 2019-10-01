# coding=utf-8

# Starting in the top left corner of a 2×2 grid, and only being 
# able to move to the right and down, there are exactly 6 routes 
# to the bottom right corner.

# right right down down
# right down right down
# right down down right
# down right right down
# down right down right
# down down right right

# |----|----|
# |    |    |
# |----|----|
# |    |    |
# |----|----|

# How many such routes are there through a 20×20 grid?

# |----|
# |    |  
# |----|
# |    | 
# |----|

# This is a dynamic programming problem (problem is a combination of sub problems optimal solutions)
# We can describe the number of paths to each spot in the grid
# as the sum of the number of paths closer to the bottom

# Base Case:
# P(0,1) = 1 (go down)
# P(1,0) = 1 (go right)
# P(2,0) = 1 

# if you are at bottom or right, there is only 1 path

# For a 1x1 grid:

# You can go right and down or down and right

# P(1,1) = 2 or 
# P(2,1) = 3 or ( P(1,1) + P(2,0))
# P(1,2) = 
# P(2,2) = 6 or ( P(1,2) + P(2,1)   )

width = 20
height = 20
grid = [[0 for i in range(width+1)] for y in range(height+1)]

# entire right side has 1 path
for y in range(height+1):
    grid[y][width] = 1

# entire bottom has 1 path
for x in range(width+1):
    grid[height][x] = 1

for y in range(height-1,-1,-1):
    for x in range(width-1,-1,-1):
        # print str(x)+","+str(y)+": " + str(grid[y+1][x]) + "+" +  str(grid[y][x+1])
        grid[y][x] = grid[y+1][x] + grid[y][x+1]

print 'Solution is ' + str(grid[0][0]) 


