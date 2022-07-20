import sys

N = int(input())

information = dict()

data = list()
for i in range(N):
    age, name = sys.stdin.readline().rstrip().split()
    data.append([int(age), name, i])

while True:
    if len(data) == 0:
        break

    data.sort()
    same_age = list()

    for k in range(len(data)):
        if data[0][0] == data[k][0]:
            same_age.append(data[k])
        else:
            pass
    same_age.sort(key = lambda x:x[2])
    for d in same_age:
        print('{0} {1}'.format(d[0], d[1]))
        data.remove(d)




