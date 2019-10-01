# https://projecteuler.net/problem=48


# Easiest to read code and is brute force solution
limit = 1000
sumOfSeries = 0
for i in range(1, limit+1):
    sumOfSeries += i**i

print sumOfSeries%int(1e10)
# 1e10 gives a float, which would try and to the mod operation
# as floating points. The numbers are too large however so an error
# is thrown


# Modular Arithmetic has some interesting properties
# (a*b) % c = ((a % c) * (b % c) )% c
# and
# (a+b) % c = ((a % c) + (b % c) )% c.

# Since we only want last 10 digits, we can cut all leading
# digits during calculations
# This helps represent the data in a smaller datatype in some
# languages

result = 0
modulo = int(1e10)

for i in range(1,1001):
    temp = i
    for j in range(1,i):
        temp *= i
        temp %= modulo
    
    result += temp
    result %= modulo

print result



