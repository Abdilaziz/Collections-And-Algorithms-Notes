import math

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

# we need lowest common multiple of the set [1 - 20]
# LCM of 2 numbers is:
# LowestCommonMultiple(x,y) = (x*y) / GCD(x,y) 

def getLCM(listOfNumb):
    answer = 1
    for i in listOfNumb:
        answer = answer * ( i // gcd(i, answer) )
    return answer


def isPalindrome(x):
    n = 0  # stores the reverse of the original number
    m = x # original number
    while x > 0:
        n = n * 10 + x % 10 # get nth digit of x (1st digit, 2nd digit, 3rd digit)
        x = x / 10 | 0 # remove first digit from x, then 2nd, etc.
    return n == m # compare reversed number with orig number

def getBinary(numb):
    return int(bin(numb)[2:])

def fib_calc(n)
    # F1 = 1, F2 = 1, F3 = 2
    # nth digit of fib sequence 
    count = 1
    x = 1  # Represents the prev Fibonacci number being processed
    y = 1  # Represents the current Fibonacci number in the sequence
    while count < n:
        x, y = y, x + y # swaps: temp = y , y = x + y, x = temp
    return y


# sequences from 1 to n that are summed are called triangle numbers
# sum of all number to n
# 1 + 2 + 3 + ..... n = n(n+1)/2

# sum of square numbers to n
# 1^2 + 2^2 + 3^2 + ... + n^2 = n(n+1)(2n+1)/6


# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	\Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...


# sum of cubes to n : https://mathschallenge.net/library/number/sum_of_cubes
# 1^3 + 2^3 + 3^3 + ... + n^3 = (n(n+1)/2)^2

# does 0.99999.... = 1 https://mathschallenge.net/library/number/point_nine_recurring

# Get all Prime Numbers under n
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers
    primeArrayOutput = []
    for p in range(2, n): 
        if prime[p]: 
            primeArrayOutput.append(p) 
    return primeArrayOutput

# Get all Prime Numbers between a and n
def SieveOfEratosthenes(a, n): 
    if a < 2:
        a = 2

    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers
    primeArrayOutput = []
    for p in range(a, n): 
        if prime[p]: 
            primeArrayOutput.append(p) 
    return primeArrayOutput

# get a list of all divisors for for numb
def getDivisors(numb):
    upperLimit = int(math.sqrt(numb)) # sqrt is upper limit
    currentDivisors = [1]
    sumOfDivisors = 1
    # consider perfect square
    if (numb == upperLimit*upperLimit):
        currentDivisors.append(upperLimit)
        sumOfDivisors += upperLimit
        upperLimit -= 1

    for i in range(2, upperLimit+1):
        if numb%i == 0:
            sumOfDivisors += i + numb/i
            currentDivisors.append(i)
            currentDivisors.append(numb/i)
    currentDivisors.sort()
    return (sumOfDivisors, currentDivisors)

def sumOfFactors(numb):
    ans = getDivisors(numb)
    return ans[0]


# more optimal way to get divisors
# Prime factorization
# Any number greater than 1 is either a prime number or a product of prime numbers
# example 12: 2,2,3

# https://mathschallenge.net/library/number/number_of_divisors


# write the number as a product of prime factors
# n = (p^a)*(q^b)(r^c).....
# Number of divisors are d(n) = (a+1)(b+1)(c+1)...
# Example: 12 = (2^2)(3^1)
# Number of divisors = (2+1)(1+1) = 6
# from 1 to sqrt(12) = 3
# divisiable by 1 (so 12) - divisable by 2 (so 6 as well), divisable by 3 (so 4 as well)

# [1,2,3,4,6,12]

# Example2: 48 = (2^4)(3^1)
# Number of divisors = (4+1)(1+1) = 10


def primeFactorizationNOD(number, listOfPrimeNumb):
    numberOfDivisors = 1
    remain = number
    for i in range(len(listOfPrimeNumb)):
        # In case there is a remainder this is a prime factor as well
        # The exponent of that factor is 1 
        if (listOfPrimeNumb[i] * listOfPrimeNumb[i] > number):
            return numberOfDivisors*2 # a is 1 so (a+1) = 2 times the rest of the divisors
        exponent = 1
        while remain%listOfPrimeNumb[i] == 0:
            exponent+=1
            remain = remain/listOfPrimeNumb[i]
        numberOfDivisors *= exponent

        if remain == 1:
            return numberOfDivisors

    return numberOfDivisors

# If you want Number of distinct prime factors
# private int NumberOfPrimeFacors(int number) {
#     int nod = 0;
#     bool pf;
#     int remain = number;
 
#     for (int i = 0; i < primeList.Length; i++) {
#         // In case there is a remainder this is a prime factor as well
#         // The exponent of that factor is 1
#         if (primeList[i] * primeList[i] > number) {
#             return ++nod;
#         }
 
#         pf = false;
#         while (remain % primeList[i] == 0) {
#             pf = true;
#             remain = remain / primeList[i];
#         }
#         if (pf){
#             nod++;
#         }
 
#         //If there is no remainder, return the count
#         if (remain == 1) {
#             return nod;
#         }
#     }
#     return nod;
# }



# Sum of divisors
# sigma(n) - sum of divisors of n
# For prime numbers: sigma(p) = 1+p
# For prime factor: sigma(p^a) =  1+p+p^2+...+p^(a)
# Multiply py p: p*sigma(p^a) = p+(p^2)+...+(p^a+1)
# Subtract the two: sigma(p^a) - sigm(p) = (p-1)sigma(p^a) = p^(a+1) -1
# Hence: sigma(p^a) = (p^(a+1) - 1)/(p - 1)

# sigma function is also multiplicative so sigma(a*b*..) = sigma(a)*sigma(b)*...
# Example: sum of divisors for 72
# sigma(72) = sigma(2^3 * 3^2) = sigma(2^3)sigm(3^2) = (2^4-1)/1 * (3^3 -1)/2 = 15*13 = 195

def primeFactorizationSOD2(number):
    listOfPrimeNumb = SieveOfEratosthenes( int(math.sqrt(number)+1) )
    # print listOfPrimeNumb
    factorsList = [1, number]
    numberOfDivisors = 1
    sumOfDivisors = 1
    remain = number
    for i in range(len(listOfPrimeNumb)):
        # print "CURRENT INDEX: " + str(i)
        # In case there is a remainder this is a prime factor as well
        # The exponent of that factor is 1
        # print "Current Prime: " + str(listOfPrimeNumb[i])
        exponent = 1
        if remain%listOfPrimeNumb[i] == 0:
            # print "FIRST: ", listOfPrimeNumb[i], remain
            p_exp = listOfPrimeNumb[i]*listOfPrimeNumb[i]
            # factorsList.append(listOfPrimeNumb[i])
            remain = remain/listOfPrimeNumb[i]
            # factorsList.append(number/listOfPrimeNumb[i])
            # print "SECOND: ", listOfPrimeNumb[i], remain
            while remain%listOfPrimeNumb[i] == 0:
                # print 'HDSDLKJLD'
                exponent+=1
                p_exp *= listOfPrimeNumb[i]
                # factorsList.append(listOfPrimeNumb[i])
                remain = remain/listOfPrimeNumb[i]
                # factorsList.append(number/listOfPrimeNumb[i])
            numberOfDivisors *= exponent
            sumOfDivisors *= (p_exp-1)/(listOfPrimeNumb[i]-1)
            # print "Sum of D: " +  str(sumOfDivisors)
            # print "Remainder: " + str(remain)

    if remain > 1:
        # remainder is a prime number greater than the sqrt(number)
        # example: if input is 10, we will have remain 5 when sqrt(10) < 5
        # print "hehe: " + str(sumOfDivisors)
        sumOfDivisors *= remain+1

    # return numberOfDivisors
    # factorsList.sort()
    # print factorsList

    # project euler isnt considering the entered number a factor
    # this is due to the fact that it is looking for proper divisors rather than just divisors.??/
    return sumOfDivisors - number 

print primeFactorizationSOD2(220)



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


# Is Permutation Check
# private bool isPerm(int m, int n) {
#     int[] arr = new int[10];
 
#     int temp = n;
#     while(temp > 0){
#         arr[temp % 10]++;
#         temp /= 10;
#     }
 
#     temp = m;
#     while(temp > 0){
#         arr[temp % 10]--;
#         temp /= 10;
#     }
 
#     for(int i = 0; i< 10; i++){
#         if(arr[i] != 0){
#             return false;
#         }
#     }
#     return true;
# }


from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

def concatNumbers(a,b):
    c = b
    while c>0:
        a *= 10
        c /= 10
    return a + b

def isPandigital(number):
    digits = 0 
    count = 0
    while number > 0:
        temp = digits
        # shifts first integer a number of places in order to add the second
        digits = digits | 1 << (number%10-1)
        if temp == digits:
            return False
        count += 1
        number /= 10
    return digits == (1 << count) -1



# Modulo Arithmetic
# https://en.wikipedia.org/wiki/Modular_arithmetic


# (a*b) % c = ((a % c) * (b % c) )% c

# and

# (a+b) % c = ((a % c) + (b % c) )% c.