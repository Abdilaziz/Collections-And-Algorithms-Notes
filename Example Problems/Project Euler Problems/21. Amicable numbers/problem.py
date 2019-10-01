# coding=utf-8

# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.


# d(n) -> get all divisors of n, then sum them
# amicable pair if d(a) = b, d(b)=  a, and a != b

# sum of all amicable numbers under 10 000

# BRUTE FORCE
# Note: We dont want to consider 220 + 280 twice, so only consider amicable sums that are higher than current digit

# run through all numbers and get sum of factors
# if sum of factors is larger than the number, 
#       then get the sum of proper divisor for the sum we just got
#       if they are the d(a) = b and d(b) = a, then we have an amicable number
# Since we iterate through all numbers, we only need to check for the sums larger than the number itself (otherwise we already checked it)

import math

def amicableSum(limit):
    sumAmicable = 0
    for i in range(2,limit+1):
        factorsSum1 = sumOfFactors(i)
        if factorsSum1 > i and factorsSum1 <= limit:
            factorsSum2 = sumOfFactors(factorsSum1)
            if factorsSum2 == i:
                sumAmicable += i + factorsSum1
    return sumAmicable

def getDivisors(numb):
    upperLimit = int(math.sqrt(numb)) # sqrt is upper limit
    currentDivisors = [1]
    sumOfDivisors = 1
    # consider perfect square
    if (numb == upperLimit*upperLimit):
        currentDivisors.append(upperLimit)
        sumOfDivisors += upperLimit
        upperLimit -= 1

    for i in range(2, upperLimit+1):
        if numb%i == 0:
            sumOfDivisors += i + numb/i
            currentDivisors.append(i)
            currentDivisors.append(numb/i)
    currentDivisors.sort()
    return (sumOfDivisors, currentDivisors)

def sumOfFactors(numb):
    ans = getDivisors(numb)
    return ans[0]

print amicableSum(10000)


# more optimal way to get divisors
# Prime factorization
# Any number greater than 1 is either a prime number or a product of prime numbers
# example 12: 2,2,3

# https://mathschallenge.net/library/number/number_of_divisors


# write the number as a product of prime factors
# n = (p^a)*(q^b)(r^c).....
# Number of divisors are d(n) = (a+1)(b+1)(c+1)...
# Example: 12 = (2^2)(3^1)
# Number of divisors = (2+1)(1+1) = 6
# from 1 to sqrt(12) = 3
# divisiable by 1 (so 12) - divisable by 2 (so 6 as well), divisable by 3 (so 4 as well)

# [1,2,3,4,6,12]

# Example2: 48 = (2^4)(3^1)
# Number of divisors = (4+1)(1+1) = 10

def primeFactorizationNOD(number, listOfPrimeNumb):
    numberOfDivisors = 1
    remain = number
    for i in range(len(listOfPrimeNumb)):
        # In case there is a remainder this is a prime factor as well
        # The exponent of that factor is 1 
        if (listOfPrimeNumb[i] * listOfPrimeNumb[i] > number):
            return numberOfDivisors*2
        exponent = 1
        while remain%listOfPrimeNumb[i] == 0:
            exponent+=1
            remain = remain/listOfPrimeNumb[i]
        numberOfDivisors *= exponent

        if remain == 1:
            return numberOfDivisors

    return numberOfDivisors

# Sum of divisors
# sigma(n) - sum of divisors of n
# For prime numbers: sigma(p) = 1+p
# For prime factor: sigma(p^a) =  1+p+p^2+...+p^(a)
# Multiply py p: p*sigma(p^a) = p+(p^2)+...+(p^a+1)
# Subtract the two: sigma(p^a) - sigm(p) = (p-1)sigma(p^a) = p^(a+1) -1
# Hence: sigma(p^a) = (p^(a+1) - 1)/(p - 1)

# sigma function is also multiplicative so sigma(a*b*..) = sigma(a)*sigma(b)*...
# Example: sum of divisors for 72
# sigma(72) = sigma(2^3 * 3^2) = sigma(2^3)sigm(3^2) = (2^4-1)/1 * (3^3 -1)/2 = 15*13 = 195

def primeFactorizationSOD(number, listOfPrimeNumb):
    # listOfPrimeNumb = SieveOfEratosthenes( int(math.sqrt(number)+1) )
    # print listOfPrimeNumb
    factorsList = [1, number]
    numberOfDivisors = 1
    sumOfDivisors = 1
    remain = number
    for i in range(len(listOfPrimeNumb)):
        # print "CURRENT INDEX: " + str(i)
        # In case there is a remainder this is a prime factor as well
        # The exponent of that factor is 1
        # print "Current Prime: " + str(listOfPrimeNumb[i])
        exponent = 1
        if remain%listOfPrimeNumb[i] == 0:
            # print "FIRST: ", listOfPrimeNumb[i], remain
            p_exp = listOfPrimeNumb[i]*listOfPrimeNumb[i]
            # factorsList.append(listOfPrimeNumb[i])
            remain = remain/listOfPrimeNumb[i]
            # factorsList.append(number/listOfPrimeNumb[i])
            # print "SECOND: ", listOfPrimeNumb[i], remain
            while remain%listOfPrimeNumb[i] == 0:
                # print 'HDSDLKJLD'
                exponent+=1
                p_exp *= listOfPrimeNumb[i]
                # factorsList.append(listOfPrimeNumb[i])
                remain = remain/listOfPrimeNumb[i]
                # factorsList.append(number/listOfPrimeNumb[i])
            numberOfDivisors *= exponent
            sumOfDivisors *= (p_exp-1)/(listOfPrimeNumb[i]-1)
            # print "Sum of D: " +  str(sumOfDivisors)
            # print "Remainder: " + str(remain)

    if remain > 1:
        # remainder is a prime number greater than the sqrt(number)
        # example: if input is 10, we will have remain 5 when sqrt(10) < 5
        # print "hehe: " + str(sumOfDivisors)
        sumOfDivisors *= remain+1

    # return numberOfDivisors
    # factorsList.sort()
    # print factorsList
    # subtract the entered number to remove it from the sum
    # this is to calculate proper divisors
    return sumOfDivisors - number
    

def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers
    primeArrayOutput = []
    for p in range(2, n): 
        if prime[p]: 
            primeArrayOutput.append(p) 
    return primeArrayOutput


def amicableSum2(limit):
    listOfPrimes = SieveOfEratosthenes( int(math.sqrt(limit)+1) )
    # print listOfPrimes
    sumAmicable = 0
    for i in range(2,limit+1):
        factorsSum1 = primeFactorizationSOD(i,listOfPrimes)
        if factorsSum1 > i and factorsSum1 <= limit:
            factorsSum2 = primeFactorizationSOD(factorsSum1, listOfPrimes)
            if factorsSum2 == i:
                sumAmicable += i + factorsSum1
    return sumAmicable

print amicableSum2(10000)