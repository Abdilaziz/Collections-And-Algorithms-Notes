# coding=utf-8

# A perfect number is a number for which the sum of its proper divisors is exactly 
# equal to the number. For example, the sum of the proper divisors of 28 would 
# be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n 
# and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
# that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
# it can be shown that all integers greater than 28123 can be written as the sum of 
# two abundant numbers. However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as the 
# sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of 
# two abundant numbers.


# Solution:
# Need to get sum of divisors (like problem 21)
# If less than number, it is defficient, greater than it is abundant, equal is perfect

# Steps
# 1) Find All abundant numbers (sum of factors is > number)
# 2) Find all the sums from the abundant numbers and store them in a list (so we know which numbers can be created from this sum)
# 3) sum all the numbers that cant be written as a sum of two abundant numbers

# Can a number be written as a sum of abundant numbers check?


import math

def getPrimeNumberList(number):

    isPrimeList = [True for i in range(number+1)]
    currentNumber = 2
    while (currentNumber*currentNumber <= number):
        if isPrimeList[currentNumber] == True:
            # update multiples of the prime number
            for i in range(currentNumber * currentNumber, number+1, currentNumber): 
                isPrimeList[i] = False
        currentNumber+=1

    primeArrayOutput = []
    for p in range(2, number): 
        if isPrimeList[p]: 
            primeArrayOutput.append(p) 
    return primeArrayOutput

def primeFactorizationSOD(number, listOfPrimeNumb):
    # listOfPrimeNumb = SieveOfEratosthenes( int(math.sqrt(number)+1) )
    # print listOfPrimeNumb
    # factorsList = [1, number]
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

def sumOfFactors(number, primeNumbers):
    return primeFactorizationSOD(number, primeNumbers)


# Int's greater than 28123 are a sum of two abundant numbers
# 
limit = 28123
primeNumbers = getPrimeNumberList(int(math.sqrt(limit)+1))
abundantList = []
for i in range(2,limit+1):
    ans = sumOfFactors(i, primeNumbers)
    if (ans > i):
        # print i, ans
        # then it is abundant
        abundantList.append(i)

# print abundantList

# Can each number be written as abundant?
# Make a list the size of the limit, each index corresponds to the number
# if that number can be expressed as a sum of 2 digits in the abundantList, mark it as True
# start second loop from i so we arent checking twice
# because its sorted ascendantly, we can stop as soon as the sum is above the limit

canBeAbundantSum = [False for i in range(limit+1)]
abundantLength = len(abundantList)
for i in range(abundantLength):
    for j in range(i, abundantLength):
        if (abundantList[i]+abundantList[j] <= limit ):
            canBeAbundantSum[ abundantList[i]+abundantList[j] ] = True
        else:
            break

sumOfNumberNotAbundant = 0
for i in range(1,limit):
    if  (canBeAbundantSum[i] == False ):
        sumOfNumberNotAbundant += i

print sumOfNumberNotAbundant
