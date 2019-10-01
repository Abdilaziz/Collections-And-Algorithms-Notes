# coding=utf-8

# Starting with the number 1 and moving to the right in a clockwise direction 
# a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# 21+7+1+3+13+17+5+9+25 = 101

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?

# 5x5 grid is a n=2 ring, (2n+1)


# (size needs to be odd for 1 to be in middle)
# for a size 5 (5/2 +1 is middle )

# Ring Function
# N is number of rings
# Example f(n) where :
# f(0) = 1

# f(1) = 
        # 7 8 9
        # 6   2
        # 5 4 3
# Width size is 2n+1
# Upper Right corner is (2n+1)^2 (n = mean top right number is 9)
# Top left corner is (2n+1)^2 - 2n
# Bottom left corner is (2n+1)^2 - 2n - 2n
# bottom right corner is (2n+1)^2 - 2n - 2n - 2n

# Sum of all 4 corners is 4(2n+1)^2 -12n
# So sum of all diagnoals = 4(2n+1)^2 -12n + f(n-1) where f(0) = 1

N = (1001 -1)/2
prevSum = 1
currSum = 0
for n in range(1, N+1):
    currSum = 4*(2*n+1)**2 - 12*n + prevSum
    prevSum = currSum
print "Answer is: " + str(currSum)


# https://www.mathblog.dk/project-euler-28-sum-diagonals-spiral/
# since we have a nice formula, we can probably fit a polynomial to get an analytical solution for f(n)
# this will make it independant of the previous ring





