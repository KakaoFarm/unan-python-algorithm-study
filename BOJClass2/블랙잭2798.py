import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
card = list(map(int, sys.stdin.readline().rstrip().split()))

combi = list()
result = list()

for i in card:
    for j in card:
        for k in card:
            if i == j or j == k or k == i:
                pass
            else:
                if i + j + k <= M:
                    combi.append(i+j +k)
# print(combi)
combi = list(set(combi))
combi.sort()
print(max(combi))
