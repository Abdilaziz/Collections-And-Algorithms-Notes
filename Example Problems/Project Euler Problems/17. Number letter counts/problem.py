# coding=utf-8


# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
# how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

# one = 3, two = 3, three = 5, four = 4, five = 4, six = 3, seven = 5, eight = 5, nine = 4
# 1-9 = 36 letters
# ten = 3, eleven = 6, twelve = 6, thirteen = 8, fourteen = 8, fifteen = 7, sixteen = 7, seventeen = 9, eighteen = 8, nineteen = 8, 
# 10-19 = 70 letters
# 20 - 99
# each prefix 10 times (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8*36 = 748

# 1-99 = 36+70+748= 854
# 100-999 
# prepend by number 1-9, then 'hundred and' (10 letters)
# then last is number 1-99
# special case is number 1-9 followed by 'hundred' (7 letters)

# 1-99 occurs 9 times: 9*854 = 7686
# 'hundred' occurs 9 times = 7*9 = 63



# etc




