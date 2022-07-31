# 곱하기 혹은 더하기
import sys

N = sys.stdin.readline().rstrip()
number_list = []
for i in N:
    number_list.append(int(i))

result = number_list[0]
for i in number_list[1:]:
    if i == 0:
        pass
    elif i == 1:
        result += 1
    else:
        if result == 0:
            result += i
        else:
            result *= i

print(result)