# coding=utf-8

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
# and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 
# 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in 
# your sum

# so that we can check if combination of multiplicand, multiplier, and product is pandigital
def concatNumbers(a,b):
    c = b
    while c>0:
        a *= 10
        c /= 10
    return a + b

def isPandigital(number):
    digits = 0 
    count = 0
    while number > 0:
        temp = digits
        # shifts first integer a number of places in order to add the second
        digits = digits | 1 << int(number%10-1)
        if temp == digits:
            return False
        count += 1
        number /= 10
    return digits == (1 << count) -1


# Now ofc we can check enitre solution space (1 to 987654321 is a waste)

# if muliplier is 4 digits, product will be at least 4 so max 4 digit is 9876
# we want digits from multiplicand + digits from multiplier + digits from product to = 9
# we can only get a combo of a 9 digit number if 

# 1 digit times a 4 digit and then product is a 5 digit.
# 2 digit times a 3 digit and product is a 4 digit

# Therefore m from 2 to 99 and 
# n from 123 or 1234 (depending on if m is 1 digit or 2) to 10 000/m 

# using a set so that we only have unique products included
productsOfPandigital = set()
sumOfProducts = 0

for m in range(2, 101):
    n_begin = 123 if m>9 else 1234
    n_end = 10000/m +1

    for n in range(n_begin, n_end):
        product = n*m
        combinedDigits = concatNumbers(concatNumbers(m,n),product)
        if (combinedDigits >= 1e8 and combinedDigits < 1e9 and isPandigital(combinedDigits)):
            productsOfPandigital.add(product)

print sum(productsOfPandigital)

