num = list(map(int, input().split()))

num.sort()
result = num[2]

while True:
    mul = 0
    for i in range(5):
        if result % num[i] == 0:
            mul += 1
            if mul == 3:
                break
        else:
            pass
    if mul == 3:
        break
    
    result += 1
    
print(result)
