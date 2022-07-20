import sys

T = int(sys.stdin.readline())
data = list()

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    data.append((H,W,N))

for d in data:
    h, w, n = d[0],d[1], d[2]

    if n % h == 0:
        last = n // h
        first = h

        if last < 10:
            room_num = '{0}0{1}'.format(first, last)
            print(int(room_num))
        else:
            room_num = '{0}{1}'.format(first, last)
            print(int(room_num))
    else:
        last = (n//h) + 1
        first = n % h
        if last < 10:
            room_num = '{0}0{1}'.format(first, last)
            print(int(room_num))
        else:
            room_num = '{0}{1}'.format(first, last)
            print(int(room_num))






