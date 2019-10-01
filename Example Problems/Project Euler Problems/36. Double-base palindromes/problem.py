# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in 
# base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include 
# leading zeros.)


def getBinary(numb):
    return int(bin(numb)[2:])

def isPalindrome(numb, b):
    # if b is base of numb
    # if b is 2, it will check if a binary number is a palindrome
    temp = numb
    result = 0
    while temp > 0:
        result =  result*b + temp%b
        temp /= b
    return result == numb

def BruteForce():
    sumOfPalindromes = 0
    limit = 1000000
    for i in range(limit):
        if isPalindrome(i, 10) and isPalindrome(i, 2):
            sumOfPalindromes += i
    return sumOfPalindromes

print BruteForce()

# we can limit the solution space by creating palindromes nu
def GeneratePalindromesSolution():

    limit = 1000000
    result = 0
    def createPalindrome(inputNumb, b, isOdd):
        n = inputNumb
        palindrome = inputNumb
        if isOdd:
            n /= b
        while n>0:
            palindrome = palindrome*b + (n%b)
            n /= b
        return palindrome
    for i in range(2):
        isOdd = True if i%2 == 0 else False
        j = 1
        numb = createPalindrome(j, 10, isOdd)
        while numb < limit:
            if isPalindrome(numb, 2):
                result += numb
            numb = createPalindrome(j, 10, isOdd)
            j+=1
    return result


print GeneratePalindromesSolution()
