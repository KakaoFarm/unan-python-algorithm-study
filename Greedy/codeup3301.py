import sys

n = int(sys.stdin.readline().rstrip())

x = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
x.reverse()
count = 0
for i in x:
    count += n // i
    n %= i
print(count)