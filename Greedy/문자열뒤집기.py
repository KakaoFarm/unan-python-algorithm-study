# 문자열 뒤집rl
from turtle import Turtle

import sys
S = sys.stdin.readline().rstrip()

d = []
for i in S:
    if i == '1':
        d.append(True)
    else:
        d.append(False)

ans = 0
for i in range(0,len(d)-1):
    if d[i] != d[i+1]:
        x = i+1
        break
while True:
    for i in range(0,len(d)-1):
        if d[i] != d[i+1]:
            x = i+1
            for j in range(x,len(d)-1):
                d[j] = not(d[j])
                if d[j] == d[j+1]:
                    ans+=1
                    break
                
                print(d)  
            break
        else:
            pass
    print(d)
    
    if d.count(True) == len(d):
        break
    if d.count(False) == len(d):
        break
    if d.count(False) == len(d)-1:
        ans += 1
        break
    if d.count(True) == len(d)-1:
        ans +=1
print(ans)
            
