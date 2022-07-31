from re import X


w = input()

word = w.upper()
dict = {}

for i in word:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

result = sorted(dict, key = lambda x: dict[x], reverse=True)
if result[0] == result[1]:
    print('?')
else:
    print(result[0])
