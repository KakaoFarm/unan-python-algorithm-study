import sys

M = sys.stdin.readline()
S = set()

for _ in range(int(M)):
    word = sys.stdin.readline().rstrip()

    if "add" in word:
        line = word.split()
        x = int(line[1])

        if x in S:
            pass
        else:
            S.add(x)

    elif "check" in word:
        line = word.split()
        x = int(line[1])

        if x in S:
            print(1)
        else:
            print(0)

    elif "toggle" in word:
        line = word.split()
        x = int(line[1])

        if x in S:
            S.remove(x)
        else:
            S.add(x)

    elif "all" in word:
        S = {i for i in range(1, 21)}

    elif "empty" in word:
        S = set()

    elif "remove" in word:
        line = word.split()
        x = int(line[1])
        if x in S:
            S.remove(x)
        else:
            pass
