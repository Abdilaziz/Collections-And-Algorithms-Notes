# The number, 197, is called a circular prime because all rotations of 
# the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


# Solution:
# I can get all primes under 1million using the sieve of eratosthenes

# how do i check if it is circular though?
# Need to use permutations function and go through circular rotations?
# check if circular rotations is under 1million, and if it is inside the 
# primeList using binary search

from collections import deque

# We can use a deque to quickly get circular rotations

def digitCount(numb):
    count = 0
    while numb > 0:
        numb /= 10
        count += 1
    return count

# under a million is 5 digits

# number = deque([2,3,5])
# for i in range(len(number)):
#     print(number)
#     number.rotate()


# We know that if the number contains an even digit, eventually it will be the last digit
# which means that it cant be a solution (primes other than 2 arent even)
# a prime number cant end in a 5 either (because then 5 would be a factor and then it wouldnt be prime)

def primeNumbers(n):
    primeCheckList = [True for i in range(n+1)]
    p = 2

    while p*p < n:
        if primeCheckList[p] == True:
            for i in range(p*p, n+1, p):
                primeCheckList[i] = False
        p += 1

    primeNumbersList = []
    for i in range(2, n+1):
        if primeCheckList[i] == True:
            primeNumbersList.append(i)
    return primeNumbersList


limit = 1000000
primeNumbersList = primeNumbers(limit)
countOfCircularPrimes = 0

for primeNumb in primeNumbersList:
    numberList = []
    temp = primeNumb
    while temp > 0:
        digit = temp%10
        temp /= 10
        numberList.append(digit)

    numb = deque(numberList)
    for i in range(len(numb)):
        if numb

        numb.rotate()
    
