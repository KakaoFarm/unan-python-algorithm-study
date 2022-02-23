import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

# 세로 길이 h-y, y-h
# 가로 길이 x-w, w-x

d1 = h-y
d2 = w-x
d3 = x
d4 = y

result =[d1, d2, d3, d4]
print(min(result))