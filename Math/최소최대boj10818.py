import sys

N = int(input())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
M = max(numbers)
m = min(numbers)
print("{0} {1}".format(m, M))