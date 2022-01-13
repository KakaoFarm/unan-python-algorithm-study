# 최소 대금 문제
import sys

pasta = []
for i in range(3):
    new_pasta = int(sys.stdin.readline())
    pasta.append(new_pasta)

juice = []
for i in range(2):
    new_juice = int(sys.stdin.readline())
    juice.append(new_juice)

choice_pasta = min(pasta)
choice_juice = min(juice)

result = round((choice_pasta + choice_juice) * 1.1,1)
print(result)
