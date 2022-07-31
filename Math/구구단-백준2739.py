N = int(input())

for i in range(1,10):
    a, b, c = N, i, N * i
    print('{0} * {1} = {2} '.format(a, b, c))