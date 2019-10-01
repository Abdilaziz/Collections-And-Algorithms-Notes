# coding=utf-8

# Euler published the remarkable quadratic formula:

# n² + n + 41

# It turns out that the formula will produce 40 primes for the consecutive values 
# n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
# and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

# Using computers, the incredible formula  n² – 79n + 1601 was discovered, which 
# produces 80 primes for the consecutive values n = 0 to 79. The product of the 
# coefficients, -79 and 1601, is -126479.

# Considering quadratics of the form:

# n² + an + b, where |a| < 1000 and |b| < 1000

# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.

# NOTE: if n = 0 results in a prime number, that means b has to be a prime number

def primeFunction(a,b,n):
    return n**2 + a*n + b

def primeNumbers(n):
    primeList = [True for i in range(n+1)]
    p = 2

    while p*p <= n:
        if primeList[p] == True:
            for i in range(p*p, n+1, p):
                primeList[i] = False
    
        p += 1
    return primeList
    # primeNumberList = []
    # for i in range(2, n+1):
    #     if primeList[i]==True:
    #         primeNumberList.append(i)

    # return primeNumberList

# Brute force solution: check every value of a and b
# Solution Space:
# a and b can be values from -1000 to 1000 
# so solution space is 2000*2000 = 4 000 000 (alot but we can do it i guess)

# Steps:
#   1) start from -1000 to 1000 for a and b
#   2) for every combination, start from n = 0 and keep going until the result isnt a prime number
#   3) keep track of a and b combo that led to the largest count of prime results

def solution1():
    limit = 1000
    maxPrimeLimitCount = 0
    maxPrimeA = 0
    maxPrimeB = 0
    # prime list needs to be long enough for us
    isPrimeList = primeNumbers(limit*limit)
    for a in range(-1*limit+1,limit+1):
        for b in range(-1*limit+1,limit+1):
            # for every AB combination, check if results are prime
            n = 0
            count = 0

            while isPrimeList[primeFunction(a,b,n)]:
                n+=1
            if n > maxPrimeLimitCount:
                maxPrimeLimitCount = n
                maxPrimeA = a
                maxPrimeB = b
    print "Longest Sequence is: " + str(maxPrimeLimitCount) + " a=" + str(maxPrimeA) + " b="+ str(maxPrimeB) + " product is: " + str(maxPrimeA*maxPrimeB)

solution1()

# Shrink the solution space
# if n = 0 , b has to be a prime number .... (shrinks from 2001 possiblilites to 336)
# if n = 1 , 1 + a + b = prime number (all primes except 2 are odd, so 1 + a + b being 
# odd means a has to be odd and b = 2 or b is odd and a is even (Much more likely)) )
# 

# def solution2():
#     limit = 1000
#     maxPrimeLimitCount = 0
#     maxPrimeA = 0
#     maxPrimeB = 0
#     # prime list needs to be long enough for us
#     isPrimeList = primeNumbers(limit*limit)
#     for a in range(-1*limit+1,limit+1):
#         for b in range(-1*limit+1,limit+1):
#             for j in range(0,1000)
#                 # for every AB combination, check if results are prime
#                 n = 0
#                 count = 0

#                 while isPrimeList[primeFunction(a,b,n)]:
#                     n+=1
#                 if n > maxPrimeLimitCount:
#                     maxPrimeLimitCount = n
#                     maxPrimeA = a
#                     maxPrimeB = b
#     print "Longest Sequence is: " + str(maxPrimeLimitCount) + " a=" + str(maxPrimeA) + " b="+ str(maxPrimeB) + " product is: " + str(maxPrimeA*maxPrimeB)





