import sys
N = int(sys.stdin.readline().rstrip())
a_n = []
for i in range(N):
    S = int(sys.stdin.readline())
    a_n.append(S)

a_n.sort()
a_n.reverse()

for i in a_n:
    print(i, end= " ")