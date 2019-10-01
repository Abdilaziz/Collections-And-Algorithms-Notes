# coding=utf-8

# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the 
# product of two 3-digit numbers.

# palindromes = []
# for i in range(100,1000):
#     for j in range(100,1000):
#         if (str(i*j) == str(i*j)[::-1] ):
#             palindromes.append(i*j)

# print max(palindromes)

# https://www.xarg.org/puzzle/project-euler/problem-4/ <- optimal solution



def isPalindrome(x):
    n = 0  # stores the reverse of the original number
    m = x # original number
    while x > 0:
        n = n * 10 + x % 10 # get nth digit of x (1st digit, 2nd digit, 3rd digit)
        x = x / 10 | 0 # remove first digit from x, then 2nd, etc.
    return n == m # compare reversed number with orig number


# product of two 3 digit numbers
# full range is from [100*100 - 999*999] = [10 000 - 998 001]
# we are looking for the largest palindrome so lets stick to 6 digits

# 'abccba' = (100 000)*a + (10 000)*b + (1 000)*c + (100)*c + (10)*b + a
#           = 11(9091a + 910b + 100c)

# so two largest numbers p * q = 11(9091a + 910b + 100c) <= 999*999
# Equation shows either p or q but not both have a factor of 11.
# In order to maximize, start searching with p = 999 and decrease p
# for each change in p, search for a max q to construct a palindrome


# Optimization: If p isn't divisible by 11, q must be so we start search with 990 as the largest
#  multiple of 11.
# Optimization: we dont need to let q go below p since we can interchange the numbers.


def solution1():
    result = 0
    s,p,q = 999
    while p>=100:

        if p%11 == 0:
            q = 999
            s = 1
        else:
            # q needs to be divisible by 11, so start at 990 (largest) and make sure each q checked is divisble by 11
            q = 990
            s = 11

        while q>99:
            prod = p*q
            if result < prod and isPalindrome(t):
                result = prod
                break
            q -= s
        p -= 1

    return result

# if we switch p and q so that p is always going to be the digit divisible by 11

def solution2():

    result = 0
    p = 990
    while p > 99:
        q = 999
        while q > 99:
            prod = p*q
            if (result < prod and isPalindrome(prod)):
                result = prod
                break
            elif prod < result:
                break
            q -= 1
        p -= 11
    return result


print solution2()