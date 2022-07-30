import sys
T = sys.stdin.readline()


for _ in range(int(T)):

    a_0 = [1, 0]
    a_1 = [0, 1]
    N = int(sys.stdin.readline())

    if N > 1:
        for i in range(N-1):
            a_0.append(a_1[-1])
            a_1.append(a_0[-2] + a_1[-1])

    print(a_0[N], a_1[N])
