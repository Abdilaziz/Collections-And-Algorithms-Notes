# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# primesFound = 0

# def isPrime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, n):
#             if n%i == 0:
#                 return False
#         return True

# currentNumber = 1
# while(primesFound != 10001):
#     currentNumber += 1
#     if isPrime(currentNumber):
#         primesFound += 1
#         # print primesFound, currentNumber

# print currentNumber



# Alternate solution

# https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 
  
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

print max(SieveOfEratosthenes(10001))

