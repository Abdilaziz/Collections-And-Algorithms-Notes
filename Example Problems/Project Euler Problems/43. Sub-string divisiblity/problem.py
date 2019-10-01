# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each 
# of the digits 0 to 9 in some order, but it also has a rather interesting sub-string 
# divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the 
# following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.


# Brute Force
# Steps: 
# 1) for every permutation of pandigital numbers
#       check if it is divisable primes 1-17
#       
def BruteForce():
    N = 10
    values = [i for i in range(N)]
    count = 1
    divisors = [1,2,3,5,7,11,13,17]
    numberOfPerm = 3265920 # 10!
    result = 0
    while count < numberOfPerm:
        # get next permutation
        i = N-1
        while values[i-1] >= values[i]:
            i -= 1
        j = N
        while (values[j-1] <= values[i-1]):
            j = j-1
        
        values[i-1], values[j-1] = values[j-1], values[i-1] # swap(i-1,j-1)
        i += 1
        j = N
        while i < j:
            values[i-1], values[j-1] = values[j-1], values[i-1] # swap(i-1,j-1)
            i += 1
            j -= 1
        count += 1
        # now values is next permutation of 0-9 pandigital number
        isDivisible = True
        for k in range(1,len(divisors)):
            number = 100*values[k] + 10*values[k+1] + values[k+2]
            if number%divisors[k] != 0:
                isDivisible = False
                break
        if isDivisible:
            number = 0
            for k in range(0, N):
                number = number*10 + values[k]
            result += number
        count += 1
    return result

print BruteForce()

# Solution:
# To get the sum of all pandigital numbers from 0 to 9, we need every pandigital number
# Every permutation from 0 to 9.... which has 10! combinations....

# So lets limit our solution space:
# d2d3d4 = divisible by 2
# d3d4d5 = divisible by 3
# etc....

# if d2d3d4 is divisible by 2, we know it has to be an even number,
# which means d4 = 0,2,4,6, or 8
# if d4d5d6 is divisible by 5
# it means that d6 = 0, 5
# d6d7d8 is divisable by 11
# But if d6 is 0, we know d7 and d8 can only be (11,22,33,etc), which we cant have
# so d6 = 5
# this means d6d7d8 is = { 506, 517, 528, 539, 561, 572, 583, 594 } (set starts with 5 and is divisable by 11 without repeating digits)




# generating all pandigital numbers with a permutations function??????








