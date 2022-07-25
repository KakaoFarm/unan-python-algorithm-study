import sys
import math

N = int(sys.stdin.readline())

fac = str(math.factorial(N))[::-1]

count = 0
for w in fac:
    if w == "0":
        count += 1
    else:
        break

print(count)
