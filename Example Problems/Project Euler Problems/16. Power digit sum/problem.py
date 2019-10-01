# coding=utf-8

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

numb = pow(2,1000)
# numb = 1873
sumOfDigits = 0 
digitIndex = 1
while numb > 0:
    sumOfDigits += numb%10 #extract lowest digit
    numb = numb/10 # remove lowest digit

print sumOfDigits


