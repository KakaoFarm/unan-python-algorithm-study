# 1부터 n까지 합 구하기
import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline().rstrip())
# 파이썬은 recursion이 1000까지 가능하다고 함.
def f(n):
    if n == 1:
        return 1
    elif n == 0:
        return  0
    else:
        return f(n-1) + n

print(f(n))
