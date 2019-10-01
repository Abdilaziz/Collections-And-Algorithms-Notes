# coding=utf-8

# By starting at the top of the triangle below and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
# 

#    3
#   7 4
#  2 4 6
# 8 5 9 3
# number of paths = 2^3 = 8
# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

#                    75
#                   95 64
#                  17 47 82
#                 18 35 87 10
#                20 04 82 47 65
#               19 01 23 75 03 34
#             88 02 77 73 07 63 67
#           99 65 04 28 06 16 70 92
#          41 41 26 56 83 40 80 70 33
#         41 48 72 33 47 32 37 16 94 29
#       53 71 44 65 25 43 91 52 97 51 14
#     70 11 33 28 77 73 17 78 39 68 17 57
#    91 71 52 38 17 14 91 43 58 50 27 29 48
#   63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
# it cannot be solved by brute force, and requires a clever method! ;o)


# How do you represent this data?
# a 2D array with zeros?

#    3
#   7 4
#  2 4 6
#  8 5 9 3

triangleRepresentation=[ [3,0,0,0], [7,4,0,0], [2,4,6,0], [8,5,9,3] ]


# Can be brute force or dynamic programming solution
# sub-problems are broken down
# Optimal Sub-structure

# Solution:
# Simplify from bottom
#    3
#   7 4
#  2 4 6
#  8 5 9 3
# becomes
#    3
#   7 4
# 10 13 15

def solveTriangle(triangle):
    numbOfLines = len(triangle)
    for i in range(numbOfLines-2, -1,-1):
        for j in range(0, i+1):
            triangle[j][i] += max( triangle[j][i+1], triangle[j+1][i+1] )
        print triangle
    return triangle[0][0]

print solveTriangle(triangleRepresentation)

# go through triangle, binary choice each time
# treeHeight = len(triangleRepresentation)
# possibleSol = pow(2,treeHeight)
# largestSum = 0
# for i in range(0,possibleSol):
#     tempSum = triangleRepresentation[0][0]
#     index = 0
#     for j in range(0,treeHeight-1):
#         tempSum += triangleRepresentation[j + 1][index]
#     if tempSum > largestSum:
#         largestSum = tempSum
# print largestSum
