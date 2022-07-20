import sys

test_case = list()

while True:
    data = sys.stdin.readline().rstrip()
    
    if data == '0':
        break
    else:
        test_case.append(data)

for data in test_case:
    compared_data = data[::-1]
    if int(data) == int(compared_data):
        print('yes')
    else:
        print('no')


'''
import sys

lines = sys.stdin.readlines()
a = lines.pop(0)[:-1]
print(a)
'''