
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by 
# all of the numbers from 1 to 20?

# we need lowest common multiple of the set [1 - 20]
# LCM of 2 numbers is:
# LowestCommonMultiple(x,y) = (x*y) / GCD(x,y) 
# LCM is commutative so LCM of set is  LCM(LCM(1,2),3)...etc.

# Note: // operator is floor division (rounds down)

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

print gcd(15,10)

answer = 1
for i in range(1,21):
    answer = answer * ( i // gcd(i, answer) )

print str(answer)