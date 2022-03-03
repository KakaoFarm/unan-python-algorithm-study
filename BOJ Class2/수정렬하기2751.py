import sys

N = int(sys.stdin.readline())

data = list()

for i in range(N):
    num = N = int(sys.stdin.readline())
    data.append(num)

data.sort()

for d in data:
    print(d)