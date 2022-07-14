import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if "push" in word:
        command = word.split()
        X = int(command[1])
        queue.append(X)

    elif "front" in word:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif "back" in word:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

    elif "size" in word:
        print(len(queue))

    elif "empty" in word:
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif "pop" in word:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
