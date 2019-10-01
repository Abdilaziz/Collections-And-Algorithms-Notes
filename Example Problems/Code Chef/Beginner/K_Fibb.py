
# T(n, k) is 1 if n <= k
# T(n, k) = T(n-1, k) + T(n-2, k) + T(n-3, k) ++++ T(n-k, k) if n > k

# recursion 
# constraints: n >= 1 , k <= 2*10^5
# Base condition: (if n<=k, return 1)
# reduction step: (n=3,k=1) ( T(3,1) = T(2,1) + T(1,1))

# cook your dish here
# M=1000000007
# a,b=list(map(int,input().split()))
# A=[1]*b
# if a<=b:
#     print(1)
# else:
#     A.append(b)
#     for j in range(b+1,a):
#         A.append((2*A[j-1]-A[j-b-1])%M)
#     print(A[-1]%M)


def k_fib(n, k):
    if (k >= 2*pow(10,5)):
        return 0
    elif (n < 1):
        return 0
    sum = 0
    if (n <= k):
        sum = 1
    else:
            sum += k_fib(i,k)
    return sum
        

# # sum = 0
print k_fib(7,5)