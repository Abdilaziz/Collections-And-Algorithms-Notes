# coding=utf-8

# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten 
# natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.


sumOfSquares = 0
squareOfSums = 0

for i in range(1,101):
    sumOfSquares += i*i
    squareOfSums += i
squareOfSums *= squareOfSums

print sumOfSquares-squareOfSums


# OR O(1) solution
# Sum of Squares is n(n+1)(2n+1)/6
# square of sums is (n(n+1)/2 )^2
