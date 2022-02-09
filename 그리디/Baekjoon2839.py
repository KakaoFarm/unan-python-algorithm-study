N = int(input())

M = N
result = 0
while M % 5 != 0:
    M = M - 3
    result += 1
    if M < 0:
        M += 3
        break

if  M % 5 != 0:
    print(-1)
else:
    result += M // 5 
    print(result)
