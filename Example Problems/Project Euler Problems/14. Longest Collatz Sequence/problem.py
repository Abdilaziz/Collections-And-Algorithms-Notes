# coding=utf-8

# Collatz conjecture is an unsolved math problem

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence 
# (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought 
# that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


# sequence length called total stopping time of n
# every number has a well-defined stopping time
# If for some n, the sequence doesn't end in 1, there is an infinite stopping time
# sequence doesn't contain one due to entering a repeated cycle, or increases without bound
# no such sequence has been found

# Examples::

# For instance, starting with n = 12, one gets the sequence 12, 6, 3, 10, 5, 16, 8, 4, 2, 1.
# n = 19, for example, takes longer to reach 1: 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1.
# The sequence for n = 27, listed and graphed below, takes 111 steps (41 steps through odd numbers, in large font), climbing to a high of 9232 before descending to 1.
# 27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1


# Thought of as a dynamic programming problem. 
# No real shortcuts here, we kinda just need to know the sequence from 1 number to the next
# however, we can cache solutions to how much steps it takes to reach 1 for each number

# Example: in the sequence starting from 13, we can break it up into a sequence starting from 
# 13 -> 5 and a sequence starting from 5 -> 1 to get the full length

# Using a solution that will cache the previous answers is key

# If you store solutions starting from the smallest number,
# we know that every time the sequence goes below the starting number,
# we have already calculated the remaining sequence length


# we want sequence length for all number up to one million

number = 1000000
startingNumberToLongestSequence = 0
longestSequence = 0

cache = [-1 for i in range(number+1)]
# steps for 1 to get to 1 is 1
cache[1] = 1
for i in range(2,number+1):
    currentNumb = i
    sequenceLength = 0
     # if number is equal to 1 stop the sequence, if number is less than the starting point, 
     # we have the sequence from there stored
    while currentNumb != 1 and currentNumb >= i:
        sequenceLength += 1
        if currentNumb%2 == 0:
            # even values are divided by 2
            currentNumb = currentNumb/2
        else:
            currentNumb = currentNumb*3 + 1
    cache[i] = sequenceLength + cache[currentNumb]

    if cache[i] > longestSequence:
        longestSequence = cache[i]
        startingNumberToLongestSequence = i

print longestSequence, startingNumberToLongestSequence
