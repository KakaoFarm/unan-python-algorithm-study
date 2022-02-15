import string

alphabets =  list(string.ascii_lowercase) # 알파벳 리스트로 불러오기


result = list()
word = input()

for i in range(len(alphabets)):
    if alphabets[i] not in word:
        result.append(-1)
    else:
        position = word.find(alphabets[i])
        result.append(position)

for i in result:
    print(i, end = " ")

