import sys

N = int(sys.stdin.readline())

info = list()
for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    info.append([x,y])

info.sort()

for coor in info:
    print("{0} {1}".format(coor[0], coor[1]))

