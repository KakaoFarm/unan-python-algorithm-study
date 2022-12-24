# import sys

# X = int(sys.stdin.readline().strip())

# count = 0 

# def operation(X :int):
#     global count

#     if X % 5 == 0:
#         X //= 5
#         count += 1
#     elif X % 3 == 0:
#         X //= 3
#         count += 1
#     elif X % 2 == 0:
#         X //= 2
#         count += 1
#     else:
#         X -= 1
#         count += 1
#     return X

# while X > 1:
#     X = operation(X)

# print(count)

'''
예시답안
'''

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 ==0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d)
print(d[x])

