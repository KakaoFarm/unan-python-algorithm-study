import sys

pos = sys.stdin.readline().rstrip()

col = ['a','b','c','d','e','f','g','h']
x = col.index(pos[0]) + 1
y = int(pos[1])


m1 = x + 2, y + 1
m2 = x + 2, y - 1
m3 = x - 2, y - 1
m4 = x - 2, y + 1
m5 = x + 1, y + 2
m6 = x + 1, y - 2 
m7 = x - 1, y + 2
m8 = x - 1, y - 2

data = [m1,m2,m3,m4,m5,m6,m7,m8]

count = 0
for i in data:
    if  1 <= i[0] <= 8:
        if 1<= i[1] <= 8:
            count += 1
        else:
            pass
    else:
        pass
print(count)
