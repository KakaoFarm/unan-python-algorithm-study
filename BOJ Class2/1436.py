# 종말의 숫자

import sys
N = int(sys.stdin.readline())

i = 1
num = 666
answer_list = []

while i <= N:
    if str(num).count('6') >= 3 and '666' in str(num):
        answer_list.append({i: num})
        i += 1

    num += 1

if N == 1:
    print(666)
else:
    print(answer_list[N-1][N])
    # print(answer_list)
