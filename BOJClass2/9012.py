import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ps = sys.stdin.readline().rstrip()

    while True:

        if "()" in ps:
            ps = ps.replace("()", "")
        else:
            break

    if len(ps) == 0:
        print("YES")
    else:
        print("NO")
