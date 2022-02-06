s = input().lstrip().rstrip().split(' ')

if '' in s:
    print(0)
else:
    print(len(s))
