import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

seq = []
i = 1
while len(seq) <= 1000:
    if seq.count(i) == i:
        i = i+1
    seq.append(i)
# print(seq)
result = 0
for n in range(A-1,B):
    result += seq[n]
    # print("result : " , result)

print(result)

