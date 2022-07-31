import sys

H, M = map(int, sys.stdin.readline().rstrip().split())


if H == 0:
    if M >= 45:
        M -= 45
    else:
        M += 15
        H = 23
    print('{0} {1}'.format(H, M))
else:
    if M >= 45:
        M -= 45
    else:
        H -= 1
        M += 15
    print('{0} {1}'.format(H, M))

