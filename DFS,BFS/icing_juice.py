# 음료수 얼려먹기
import sys
from collections import deque

N, M = sys.stdin.readline().rstrip().split()

graph = []
for i in range(int(N)):
    x = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    graph.append(x)

print(graph)