N = int(input())

words = list()

for i in range(N):
    word = input()
    words.append(word)

result = list(set(words))
result.sort()
result.sort(key = len)

for r in result:
    print(r)


