import sys

scale = list(map(int, sys.stdin.readline().rstrip().split()))

j1 = sorted(scale)
j2 = sorted(scale, reverse=True)

if scale == j1:
    print("ascending")
elif scale == j2:
    print("descending")
else:
    print("mixed")
