
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# Prime number can only be factored by itself and by 1
#  ex. 17 can only be divided by 17 and 1
# 1) Only even prime number is 2 (everything else can be divided by 2)
# 2) No prime number greater than 5 ends in 5 (if it does it can be divided by 5)
# 3) 0 and 1 are not prime numbers
# 4) If its not prime (or 0 and 1), it is called composite

# factor of number 
import math 
  
# A function to find largest prime factor 
def maxPrimeFactors (n): 
      
    # Initialize the maximum prime factor 
    # variable with the lowest one 
    maxPrime = -1
      
    # Print the number of 2s that divide n 
    while n % 2 == 0: 
        maxPrime = 2
        n = n/2
          
    # n must be odd at this point,  
    # thus skip the even numbers and  
    # iterate only for odd integers 

    # if a*b=n and a> sqrt(n) and b> sqrt(n) then a*b > sqrt(n)*sqrt(n)
    # which contradicts a*b = n

    # To prove that this optimization works, let us consider the following 
    # property of composite numbers.

    # Every composite number has at least one prime factor less than or 
    # equal to square root of itself.

    # This property can be proved using counter statement. Let a and b 
    # be two factors of n such that a*b = n. If both are greater than √n, 
    # then a.b > √n, * √n, which contradicts the expression “a * b = n”.


    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
      
    # This condition is to handle the  
    # case when n is a prime number  
    # greater than 2 
    if n > 2: 
        maxPrime = n 
      
    return int(maxPrime) 
  
# Driver code to test above function 
n = 15
print(maxPrimeFactors(n)) 
  
n = 600851475143
print(maxPrimeFactors(n)) 