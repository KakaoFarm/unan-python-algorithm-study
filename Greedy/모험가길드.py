# 모험가 길드
import sys

N = int(sys.stdin.readline().rstrip())
phobia = list(map(int,sys.stdin.readline().rstrip().split()))

group_number = 0
for i in phobia:
    if i == 1:
        group_number += 1
        phobia.remove(i)

phobia.sort()
group = []
for i in phobia:
    group.append(i)
    if len(group) == i:
        if max(group) > len(group):
            group = []
        else:
            group_number += 1
            group = []

print(group_number)