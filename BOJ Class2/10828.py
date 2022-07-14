import sys
from collections import deque

N = int(sys.stdin.readline())
stack = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip()

    if "push" in command:
        X = int(command.split()[1])
        stack.append(X)

    elif "pop" in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif "size" in command:
        print(len(stack))

    elif "empty" in command:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "top" in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
