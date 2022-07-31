n = input()
sum = 0

for i in n:
    sum += int(i)

if sum % 3 == 0:
    print(1)
else:
    print(0)