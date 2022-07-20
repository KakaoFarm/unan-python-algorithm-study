from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
sample_deque = deque()

for _ in range(N):
    command = sys.stdin.readline().rstrip()

    if "push_back" in command:
        c = command.split()
        X = int(c[1])
        sample_deque.append(X)

    elif "push_front" in command:
        c = command.split()
        X = int(c[1])
        sample_deque.appendleft(X)

    elif "pop_front" in command:
        if len(sample_deque) == 0:
            print(-1)
        else:
            print(sample_deque.popleft())

    elif "pop_back" in command:
        if len(sample_deque) == 0:
            print(-1)
        else:
            print(sample_deque.pop())

    elif "size" in command:
        print(len(sample_deque))

    elif "empty" in command:
        if len(sample_deque) == 0:
            print(1)
        else:
            print(0)
    elif command == "front":
        if len(sample_deque) == 0:
            print(-1)
        else:
            print(sample_deque[0])
    elif command == "back":
        if len(sample_deque) == 0:
            print(-1)
        else:
            print(sample_deque[-1])
