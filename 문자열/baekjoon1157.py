# 1157. 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
w = input()

word = w.upper()
dict = {}

for i in word:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

result = sorted(dict.items(), key = lambda x: x[1], reverse=True)
if len(result) == 1:
    print(result[0][0])
else:
    if result[0][1] == result[1][1]:
        print('?')
    else:
        print(result[0][0])