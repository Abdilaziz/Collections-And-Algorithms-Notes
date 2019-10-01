# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

# def isPrime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2,n):
#             if n%i == 0:
#                 return False
#         return True

# sumOfPrimes = 0
# for i in range(1, 2000000):
#     if isPrime(i):
#         sumOfPrimes += i
# print sumOfPrimes


# ABOVE IS TOO SLOW, SIMPLE SOLUTION FOR SMALLER n

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
  
# driver program 
if __name__=='__main__': 
    n = 2000000
    print "Following are the prime numbers smaller", 
    print "than or equal to", n 
    print sum(SieveOfEratosthenes(n))