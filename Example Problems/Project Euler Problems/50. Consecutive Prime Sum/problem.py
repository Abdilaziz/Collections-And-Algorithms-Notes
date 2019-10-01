# coding=utf-8

# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

# Steps:
#   1) Having a list of sums of prime numbers would be useful to get the sum of a consecutive order
#       allows us to get sum of primes between 11 and 3 ( f(11) - f(3)  )
#   2) search for the greatest sum that is a prime numb

def primeNumbers(n):
    isPrime = [True for i in range(n+1)]
    p = 2
    while p*p<=n:
        if isPrime[p]== True:
            for i in range(p*p, n+1, p):
                isPrime[i] = False
        p+=1

    primeNumbers = []
    for i in range(2,n+1):
        if isPrime[i] == True:
            primeNumbers.append(i)
    return primeNumbers

def primeSums(primeNumbs):
    primeSums = [0 for i in range(len(primeNumbs)+1)]
    for i in range(len(primeNumbs)):
        primeSums[i+1] = primeSums[i] + primeNumbs[i]
    return primeSums

from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

limit = 1000000
result = 0
numbOfPrimes = 0
primes = primeNumbers(limit)
primeSum = primeSums(primes)

# from 0 - limit
for i in range(numbOfPrimes, len(primeSum)):
    for j in range( i - (numbOfPrimes+1) , -1, -1):
        
        # we want a prime below a million that can be written as athe sum of the most consecutives
        # so if we reach a sum that is larger than the limit, break out of the inner loop
        if (primeSum[i] - primeSum[j] > limit):
            break
        if BinarySearch(primes, primeSum[i] - primeSum[j]) >= 0:
            numbOfPrimes = i - j
            result = primeSum[i] - primeSum[j]

print numbOfPrimes, result


