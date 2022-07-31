#큰 수의 법칙 문제

(N, M ,K) = tuple(map(int,input().split()))
numbers = list(map(int, input().split()))

numbers.sort()
numbers.reverse()

def Law(N,M,K):
    sum = 0
    turn = 0
    while turn < M:
        count = 0
        while count < K:
            turn += 1
            if turn == M:
                break
            sum += numbers[0]
            count +=1          
        
        sum += numbers[1]
        if turn != M:
            turn +=1
        
    return sum

print(Law(N,M,K))