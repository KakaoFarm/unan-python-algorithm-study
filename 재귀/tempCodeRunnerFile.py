# 1부터 n까지 합 구하기
import sys
n = int(sys.stdin.readline().rstrip())

def f(n):
    if n == 1:
        return 1
    elif n == 0:
        return  0
    else:
        return f(n-1) + n

print(f(n))