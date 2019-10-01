# coding=utf-8

# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following 
# expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# Solution
# f(1)=1
# f(2)=2
# f(3)=3
# f(4)=4
# .... 
# f(10)=1
# f(11)=0
# f(12)=1
# f(13)=1
# f(14)=1
# f(15)=2
# f(16)=1
# f(17)=3
# f(18)=1
# f(19)=4
# f(20)=1
# f(21)=5

# n <10
# f(n) = n
# 10<= n <= 20
# f(n) = if even (1), if odd ( (n-1)/2 ) ( last digit -1 divide by 2 )

# 10<= n <= 20
# 10 number of 2 digits each so 20 digits are covered
# 10 to 30 is covered, so 
# 15 starts on 20
# 20 starts on 30
# 25 starts on 40
# so 100 starts on 190?? (5 each )

# 1-9: 1-9
# 10-99: 10-189
# 100-999: 190-2.889
# 1.000-9.999:  2.890-38.889
# 10.000-99.999: 38.890 – 488.889
# 100.000-999.999: 488.890 – 5.888.889









