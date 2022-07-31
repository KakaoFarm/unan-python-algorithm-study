
N = int(input())
string_list = list()
for i in range(N):
    string = input()
    string_list.append(string)

def score(n):
    return int(n * (n+1) / 2)

for word in string_list:
    result = 0
    count = 0
    for i in range(len(word)):
        if word[i] == 'O':
            count += 1
            if i ==  (len(word)-1):
                result += score(count)
        else:
            if count == 0:
                pass
            else:
                result += score(count)
                count = 0
    print(result)

