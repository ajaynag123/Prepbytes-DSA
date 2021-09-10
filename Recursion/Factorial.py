import sys
sys.setrecursionlimit(10000)
n = int(input())

def factorial(n):
    if n<0:
        return 'enter value greater than or equal to zero'
    if n ==0 or n==1:
        return 1

    smallOutput = factorial(n-1)

    return n*smallOutput    


print(factorial(n))    