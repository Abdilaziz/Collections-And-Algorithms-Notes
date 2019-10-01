
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# Brute Force
# Check if a number is equal to the sum of factorial of its digits.



# Limit Soultion Space:
# We can limit the solution space by thinking about what the limit is
# 
# Max digit is 9!*7 = 2540160, because 9!*8 is also a 7 digit number

# Pre Calculate Factorials

def factorial(x):
    if x == 0:
        return 1
    y = x
    for i in range(1,x):
        y *= i
    return y


result = 0
limit = 2540160
factorialsCalculated = [ factorial(i) for i in range(10) ]
for i in range(10, limit+1):
    sumOfFactorials = 0
    number = i
    while number > 0:
        digit = number%10
        number /= 10
        sumOfFactorials += factorialsCalculated[digit]
    if sumOfFactorials == i:
        result += i

print "Answer is: " + str(result)


