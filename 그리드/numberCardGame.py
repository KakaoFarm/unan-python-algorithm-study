# 숫자 카드 게임
import random

N, M = list(map(int, input().split()))
result = [] # 각줄 가장 작은 값

for i in range(N): # 행 별로 줄을 가져오기 위한 반복
    data = list(map(int,input().split())) # 각 행 값
    min_value = min(data) # 행의 최소 값
    result.append(min_value) # 최소값을 result list 추가

print(max(result)) # 그 중 가장 큰 값



