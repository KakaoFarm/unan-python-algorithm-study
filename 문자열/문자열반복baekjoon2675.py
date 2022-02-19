T = int(input())

data = list()
for i in range(T):
   R,  S = tuple(input().split())
   data.append((R,S))

for case in data:
    n = int(case[0])
    word = ""
    for i in range(len(case[1])):
        word += case[1][i] * n
    print(word)


