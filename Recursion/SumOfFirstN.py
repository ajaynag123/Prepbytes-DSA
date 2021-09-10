import sys
sys.setrecursionlimit(1000)
n = int(input())

def sumOfN(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    smallOutput = sumOfN(n-1)

    return n+smallOutput        



print(sumOfN(n))    