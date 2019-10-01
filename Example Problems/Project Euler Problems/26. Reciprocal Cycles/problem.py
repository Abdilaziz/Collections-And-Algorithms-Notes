# coding=utf-8

# A unit fraction contains 1 in the numerator. The decimal 
# representation of the unit fractions with denominators 
# 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring 
# cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the 
# longest recurring cycle in its decimal fraction part.

# Python float division is with ./
# 1./7 is 0.(142857)(142857)14285
# How do we approach this because the float division in python has limitations...
# An approach is:
# Instead of calculating the fraction, analyze the remainder on each position


# print 1./7
# print 1%7
# with 1 remainder, we analyse the remainder on the first decimal place by
# multiply by 10 and divide by 7
# print 1) 10%7
# answer is 3, so lets do 30/7
# print 2) 30%7
# answer is 2, so 3) 20/7
# print 4) 20%6
# answer is 6. then 5) 60/7 is 4, then 6) 40/7 is 5, then 7) 50/7 is 1
# keep going until you see 1 again.
# then you will know if you continue the pattern will continue
# Thus the longest recurring cylce has been found:
# 7 steps - 1 = 6 digits long

# NOTE: the max recurring cycle length in 1/d is d-1
# that means more chance to find large recurring cycle when d is large
# Also means we can stop search when d becomes lower than the longest cycle we have found


# Find the value of d < 1000 for which 1/d contains the 
# longest recurring cycle in its decimal fraction part.
upperLimit = 1000
sequenceLength = 0
for d in range(upperLimit-1, 1, -1):
    if sequenceLength >= d:
        # will never find a sequence longer than the one we already found for lower numbers
        break

    remaindersAcquired = [0 for i in range(d)] # create d sized array to store remainders (max can only be d-1)

    curValue = 1
    position = 0
    while remaindersAcquired[curValue] == 0 and curValue != 0:
        remaindersAcquired[curValue] = position
        curValue *= 10
        curValue %= d
        position += 1
    if (position - remaindersAcquired[curValue] > sequenceLength):
        sequenceLength = position - remaindersAcquired[curValue]


print "Longest Cycle happens: " + str(position) + " and has length of " + str(sequenceLength)  



