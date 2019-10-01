# coding=utf-8

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# Get factorial, then sum the digits

import math

# 100! is a huge number, so data types need to be considered in some languages
value = math.factorial(100)

def fact(numb):
    factorial = 1
    for i in range(2,numb+1):
        factorial *= i
    return factorial

value2 = fact(100)

def addDigits(numb):
    digitSum = 0
    while numb > 0:
        digitSum += numb%10
        numb = numb/10
    return digitSum



print addDigits(value)
print addDigits(value2)



