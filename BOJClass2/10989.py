# 10989 수 정렬하기 3
import sys

N = int(sys.stdin.readline())

numbers = [0] * 10100

for i in range(N):
    num = int(sys.stdin.readline())
    numbers[num] += 1


for idx in range(10001):
    if numbers[idx] != 0:
        for j in range(numbers[idx]):
            print(idx)
