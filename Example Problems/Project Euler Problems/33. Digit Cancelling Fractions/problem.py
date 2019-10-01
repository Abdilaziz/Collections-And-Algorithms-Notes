# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify 
# it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

# https://www.mathblog.dk/project-euler-33-fractions-unorthodox-cancelling-method/

import math

def primeNumbers(n):
    isPrimeList = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if isPrimeList[p] == True:
            for i in range(p*p, n+1, p):
                isPrimeList[i]= False
        p += 1

    primeNumbers = []
    for i in range(2, n+1):
        if isPrimeList[i] == True:
            primeNumbers.append(i)    

    return primeNumbers

def primeFactorizationSOD(number):
    listOfPrimeNumb = primeNumbers( int(math.sqrt(number)+1) )
    factorsList = {1,number}
    sumOfDivisors = 1
    remain = number
    for i in range(len(listOfPrimeNumb)):
        if remain%listOfPrimeNumb[i] == 0:
            p_exp = listOfPrimeNumb[i]*listOfPrimeNumb[i]
            remain = remain/listOfPrimeNumb[i]
            factorsList.add(listOfPrimeNumb[i])
            factorsList.add(remain)
            while remain%listOfPrimeNumb[i] == 0:
                p_exp *= listOfPrimeNumb[i]
                remain = remain/listOfPrimeNumb[i]
            sumOfDivisors *= (p_exp-1)/(listOfPrimeNumb[i]-1)

    if remain > 1:
        sumOfDivisors *= remain+1

    # project euler isnt considering the entered number a factor
    # this is due to the fact that it is looking for proper divisors rather than just divisors.??/
    print sorted(factorsList)
    return sumOfDivisors - number 

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a, a)





