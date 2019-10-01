# coding=utf-8


# In England the currency is made up of pound, £, and pence, p, and there are 
# eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

# target = 200
# ways = 0
# for a in range(target,-1,-200):
#     for b in range(a, -1, -100):
#         for c in range(b, -1, -50):
#             for d in range(c, -1, -20):
#                 for e in range(d, -1, -10):
#                     for f in range(e, -1, -5):
#                         for g in range(f, -1, -2):
#                             ways += 1

# print ways



# Dynamic Programming

# if 1p is target you can only give 1p
# if 2p is target, we can give 2 1p's or 1 2p
# if 3p is target we can give 3 1ps or 1 2p and 1 1p

# So solution for scalculated 1p is used to get ways to calculate 2p, etc
# Run time for dynamic programming solution is much better for larger targets

target = 200
coinSizes = [1,2,5,10,20,50,100,200]

ways = [0 for i in range(target+1)]
ways[0]=1
for i in coinSizes:
    for j in range(i, target+1):
        ways[j] += ways[ j - i ]
print ways[target]