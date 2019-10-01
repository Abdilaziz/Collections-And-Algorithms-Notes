# coding=utf-8


# It was proposed by Christian Goldbach that every odd composite number can be written 
# as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and 
# twice a square?


# Every Odd Composite Number
    # Every odd number that isnt a prime number
# Is sum of prime and twice a square (of a prime?: Nope guess not)

# make list of prime numbers (with true and false per index)
# go through each odd composite number (odd number that is false) and check to see if
# that value minus a prime number is divisable by a prime number..

# stop on the first odd composite that cant be written as the


def BruteForce():
    limit = 1000
    result = 0
    primeNumbers = [True for i in range(limit+1)]
    p = 2
    while p*p < limit:
        if primeNumbers[p] == True:
            for i in range(p*p, limit+1, p):
                primeNumbers[i] = False
        p +=1

    primeList = []
    for i in range(2,limit+1):
        if primeNumbers[i] == True:
            primeList.append(i)

    for oddNumb in range(1,limit+1,2):
        if primeNumbers[oddNumb] == False:
            # check if it is divisiable by a prime number
            foundPrimes = False
            for prime1 in primeList:
                for prime2 in primeList:
                    if ((oddNumb-prime1) - 2*prime2*prime2) == 0:
                        foundPrimes = True
                        break
                if foundPrimes:
                    break
            if foundPrimes == False:
                result = oddNumb
                break
    return result

# print BruteForce()

from math import sqrt

def isTwiceSquared(number):
    squareTest = sqrt(number/2)
    return squareTest == int(squareTest)

def sieveOfErasthothenes(limit):
    primeNumbers = [True for i in range(limit+1)]
    p = 2
    while p*p < limit:
        if primeNumbers[p] == True:
            for i in range(p*p, limit+1, p):
                primeNumbers[i] = False
        p +=1

    primeList = []
    for i in range(2,limit+1):
        if primeNumbers[i] == True:
            primeList.append(i)

    return primeList

def Method2():
    primeList = sieveOfErasthothenes(10000) 
    result = 1
    notFound = True

    while notFound:
        result +=2 # NEXT ODD NUMBER
        j = 0
        notFound = False
        while result >= primeList[j]:
            if isTwiceSquared(result - primeList[j]):
                notFound = True
                break
            j += 1
    return result

print Method2()