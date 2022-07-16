import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().rstrip().split()))

queue = deque(i for i in range(1, N+1))
numbers = []

while len(queue) != 0:
    for i in range(K-1):
        queue.append(queue.popleft())
    numbers.append(queue.popleft())

result = ", ".join(str(n) for n in numbers)
print(f"<{result}>")
