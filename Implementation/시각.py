# 시각 문제
#00:00:00 ~ N:59:59까지
# 1 ~ 60초 까지 3이 있는 경우 :15번
# 1 ~ 60초 까지 3이 없는 경우 :45번
# 분에서 3이 없는 경우는 45번 x 15번
# 분에서 3이 있는 경우는 60번 x 15번
#시에서 3이 있는 경우는 60x60 = 3600
#시에서 3이 없는 경우는 15x45 + 60x15
import sys
N = sys.stdin.readline().rstrip()
def solution(N):
    ans = 0
    for i in range(int(N)+1):
        if '3' in str(i): 
            ans += 60 * 60
            
        else:
            ans += 15*45 + 60*15     
    return ans

print(solution(N))

             