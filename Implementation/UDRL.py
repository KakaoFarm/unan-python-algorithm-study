# 상하좌우 문제
import sys

N = int(sys.stdin.readline())
plan = sys.stdin.readline().rstrip().split()

position = [1,1]
for i in range(len(plan)):
    if plan[i] == 'U':
        if position[0] == 1:
            pass
        else:
            position[0] -= 1
    
    elif plan[i] =='D':
        if position[0] == N:
            pass
        else:
            position[0] += 1
    elif plan[i] =='R':
        if position[1] == N:
            pass
        else:
            position[1] += 1
    else:
        if position[1] == 1:
            position[1] -= 1
    
print('{0} {1}'.format(position[0],position[1]))