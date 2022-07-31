T = int(input())
case = []
for i in range(T):
    N, M = list(map(int, input().split()))
    case.append((N,M))


# 조합 구현
def fac(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fac(n-1) * n

def combi(n,r):
    return fac(n) / (fac(r) * fac(n-r))

for i in case:
    print(int(combi(i[1],i[0])))

