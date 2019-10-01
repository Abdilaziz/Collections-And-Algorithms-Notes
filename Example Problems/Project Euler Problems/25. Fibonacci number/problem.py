# coding=utf-8

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# Brute Force Steps:
# 1) find fibonacci sequence from bottom up and cache prev reusult and current
# 2) keep going until it has 1000 digits i guess

# CHecking digits every loop is very slow, so just compare two integers
# 10^999 

# Pen and Paper
# for large enough fibonacci numbers, they converge: https://www.mathblog.dk/project-euler-25-fibonacci-sequence-1000-digits/


import math
# def numbOfDigits(n):
#     # Due to floating point inaccuracies, using log solution only works for numbers
#     # smaller than 999999999999997 (result will round up)
#     if n <= 999999999999997:
#         return int(math.log10(n)) + 1
#     else:
#         counter = 15
#         while n >= 10**counter:
#             counter += 1
#         return counter

ans = 0
curIndex = 2
x = 1  # Represents the current Fibonacci number being processed
y = 1  # Represents the next Fibonacci number in the sequence
upperLimitDigits = 1000
# limit = 10**upperLimitDigits
upperBoundry = 10**(upperLimitDigits-1)
# while numbOfDigits(x) != limit: # checking digits every time is very slow
while y <= upperBoundry:
    curIndex += 1
    x, y = y, x + y # swaps: temp = y , y = x + y, x = temp

print curIndex

