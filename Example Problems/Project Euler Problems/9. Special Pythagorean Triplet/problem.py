# A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


for i in range(1, 1001):
    for j in range(1, i):
        for k in range(1, j):
            if ( (k*k + j*j) == i*i  and ( (i + j + k) == 1000 ) ):
                print k,j,i, i*j*k


# PERIMETER = 1000
# for a in range(1, PERIMETER + 1):
# 	for b in range(a + 1, PERIMETER + 1):
# 		c = PERIMETER - a - b
# 		if a * a + b * b == c * c:
# 			# It is now implied that b < c, because we have a > 0
# 			return str(a * b * c)




