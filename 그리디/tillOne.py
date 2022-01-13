import sys
N, K = list(map(int, sys.stdin.readline().rstrip().split()))

def till_one(N,K):
    count = 0

    while N != 1:
        if N % K != 0:
            N -= 1
            count += 1
        else:
            N //= K
            count += 1

    return count        

print(till_one(N,K))