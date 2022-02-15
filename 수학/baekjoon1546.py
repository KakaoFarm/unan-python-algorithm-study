import sys

N = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))

first_rank = max(num)

new_num =[]
for i in num:
    x = (i / first_rank) * 100
    new_num.append(x)

result = sum(new_num) / N
print(result)