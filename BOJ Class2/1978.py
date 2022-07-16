import math
import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

prime_numbers = []

for i in range(2, 1001):
    prime = True
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            prime = False

    if prime:
        prime_numbers.append(i)

count = 0

for num in numbers:
    if num in prime_numbers:
        count += 1

print(count)
