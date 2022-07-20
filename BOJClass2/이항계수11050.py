import sys
N, K = map(int, sys.stdin.readline().rstrip().split())


def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return factorial(n-1) * n


def combination(n,k):
    return int(factorial(n) / (factorial(k) * factorial(n-k)))


print(combination(N,K))