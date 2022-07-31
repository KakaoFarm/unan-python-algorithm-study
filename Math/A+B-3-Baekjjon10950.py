import sys

T = int(sys.stdin.readline().rstrip())

numbers = list()
for i in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    numbers.append((A,B))

for x in numbers:
    print(x[0] + x[1])