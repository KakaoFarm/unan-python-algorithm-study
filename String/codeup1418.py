from cgi import print_form
import sys

word = sys.stdin.readline().rstrip()

t_list = []
for i in range(len(word)):
    if word[i] == 't':
        t_list.append(str(i+1))

result = ' '.join(t_list)
print(result)
