

"""

Given a 2D matrix M of 0's and 1

Count number of islands, in the matrix
Island is a group of 1's  or a 1 by itself



[  [ 1, 0, 1  ],
   [ 0, 1, 1  ]  ]

# 1) Clarify Question (include diagnoals?)

# 2) Confirm Inputs ()
        Input is matrix
        Output is number of islands in the matrix

# 3) Test Cases
        Inputs : None, [[]] (empty matrix)
        Confirm first matrix as well
        Can values be in the matrix as well?

# 4) Brainstorm
        If input is [[]] or None, return 0 because there are no islands

        # start at first index, initialize island counter
        # We need to keep track of which 1's are a part of the same island
        # Check edge cases before you check if it is a 1 or a 0

        Matrix could be representation of a graph (Adjacency matrix),
        this is a breadth first search problem.

        When you find the first 1,
        look at elements around it,
        add those elements to a queue,
        check if those are 1,
            If yes, set them to another number so we know it is 
            visited

# 5) Runtime analysis
        - looking at every element in this matrix, at least once
        run time will be MxN (row vs column)

# 6) Coding
        - explain your code while writting rather than just
        the syntax

# 7) Debugging
        - check syntax and check test cases

"""

from collections import deque

def islandCounter(M):
    if M == None or M == [[]]:
        return 0
    islands = 0
    rowNumb = len(M)
    colNumb = len(M[0])
    for m in range(0, rowNumb):
        for n in range(0,colNumb):
            if M[m][n] == 1:
                islands += 1
                findPartsOfIsland(M, m, n, rowNumb, colNumb)
    return islands

def findPartsOfIsland(M, m, n, rowNumb, colNumb):
    a = deque()
    a.append([m,n])
    while len(a) != 0:
        # check elements around it
        temp = a.pop()
        m = temp[0]
        n = temp[1]
        if M[m][n] == 1:
            M[m][n] = 2
            appendIf( a, rowNumb, colNumb, m +1, n )
            appendIf( a, rowNumb, colNumb, m-1, n )
            appendIf( a, rowNumb, colNumb, m, n+1 )
            appendIf( a, rowNumb, colNumb, m, n-1 )


def appendIf(a, rowNumb, colNumb, m, n):
    if m > 0 and m < rowNumb and n > 0 and n < colNumb:
        a.append([m,n])

if __name__ == "__main__":
    M = [[1,0,1],
     [0,1,1],
     [1,0,0]]

    print islandCounter(M)
