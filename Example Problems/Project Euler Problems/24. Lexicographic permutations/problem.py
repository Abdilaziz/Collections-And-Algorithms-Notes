# coding=utf-8


# A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
# permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed 
# numerically or alphabetically, we call it lexicographic order. The lexicographic 
# permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the 
# digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# if a number has 3 digits, it can be rearranged into how much permutations?
# if its 1 digit -> 1 permutation
# 2 digits -> 2 permutations
# 3 digits -> 6 permutations
# 4 digits -> 24 permutations

# Factorial (digits) = number of permutations
# so for brute force would be really slow for most number of digits ( 7! = 5040 )
# we want 10! which is 3 628 800

# Does lexicographic representation have an order?
# IDK...

# Algorithm to generate permutations is called cut-the-knot
# https://www.cut-the-knot.org/do_you_know/sgroups.shtml#symmetric
# http://www.cut-the-knot.org/do_you_know/AllPerm.shtml

# Every permutations can be represented as a product of cycles
# n = number of digits
# n= 3 -> 6 permutations or a list of 6 elements of the symmetric group S3
# 

#    1
#   2  3

# Observing permutations as products of cycles makes it obvious that elements of S3
# represent rigid motions of an equilateral triangle
# Imagine a triangle with vertices labeled 1,2,3 so (1,2,3) denotes a rotation of vertices
# where 1 goes to 2, 2 goes to 3, 3 goes to 1
# (1,3,2) is a rotation in the opposite direction
# (1,2)(3) is the symmetry around the median from vertex 3

# N is the number of items to be permuted
# Recursive solution

permutations = []
level = -1
def recursive_solution(N):
    print 'Recursive:'
    valueList = [0 for i in range(N)] # array of 0's
    def visit(k):
        global level
        # print level
        level += 1
        valueList[k] = level  
        if level == N:
            permutations.append(str(valueList))
            # print valueList
        else:
            for i in range(N):
                if valueList[i] == 0:
                    visit(i)
        level = level-1
        valueList[k] = 0
    visit(0)

# recursive_solution(3)
# print permutations

# Lexicographic Solution
# Permutation f preceed permutation g in lexicographic (alphabetic) order
# if and only if for the min value of k such that f(k)!=g(k) we have f(k)<g(k)
# Starting with identical permutation f(i)=i for all i, second algorithm generates
# sequntially permutations in the lexicographic order
permutations = []
def lexicographic_solution(N):
    print 'Lexicographic:'
    values = [x for x in range(1,N+1)]
    def getNext():
        print(values)
        i = N-1
        while values[i-1] >= values[i]:
            i -= 1
        j = N
        while (values[j-1] <= values[i-1]):
            j = j-1
        
        values[i-1], values[j-1] = values[j-1], values[i-1] # swap(i-1,j-1)
        # print(values)
        i += 1
        j = N
        while i < j:
            values[i-1], values[j-1] = values[j-1], values[i-1] # swap(i-1,j-1)
            # print(values)
            i += 1
            j -= 1
    getNext()
    getNext()
    getNext()
    getNext()
    getNext()
    getNext()
    getNext()
    getNext()

# lexicographic_solution(3)


# so using the lexicographic_solution

N = 10
values = [i for i in range(N)]
count = 1
numberOfPerm = 1000000

while count < numberOfPerm:
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

# Millionth permutation is:

print ''.join(str(e) for e in values)
