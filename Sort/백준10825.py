import sys

N = int(sys.stdin.readline())

data = []
for _ in range(N):
    d = list(sys.stdin.readline().rstrip().split())
    data.append(d)

for d in data:
    for i in range(1, len(d)):
        d[i] = int(d[i])
new_data = sorted(data, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for d in new_data:
    print(d[0])
