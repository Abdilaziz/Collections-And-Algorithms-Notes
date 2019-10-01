# coding=utf-8


# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4

# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Brute Force
# need an upper bound.

# We know that for a sum of fifth powers of their digits
# Solution Space: we are adding 5 digits of a power of 5

# Max value is 9^5 + 9^5 + 9^5 + 9^5 + 9^5 = 295245 
# so we need to make a 6 digit number to represent the sum

# 6* 9^5 = 354294
# Lets just say 355 000

totalSum = 0
for i in range(2, 355000):
    sumOfPowers = 0
    number = i
    while number > 0:
        d = number % 10 # last digit
        number /= 10 # remove last digit from number
        sumOfPowers += d**5
    if sumOfPowers == i:
        totalSum+=i

print totalSum