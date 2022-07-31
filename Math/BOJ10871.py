import sys

N, X = map(int,  sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

result = list()

for component in A:
    if component < X:
        result.append(component)
    else:
        pass

for i in result:
    print(i, end = " ", sep= " ")