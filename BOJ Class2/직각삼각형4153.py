import sys


data = list()
while True:
    A,B,C = map(int,sys.stdin.readline().rstrip().split())
    if (A,B,C) == (0,0,0):
        break
    data.append((A,B,C))

for length in data:
    if  2* (max(length) ** 2) == (length[0] ** 2) + (length[1] ** 2) + (length[2] ** 2):
        print('right')
    else:
        print('wrong')