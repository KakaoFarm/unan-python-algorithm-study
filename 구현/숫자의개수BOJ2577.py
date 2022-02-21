A = int(input())
B = int(input())
C = int(input())

multiple = str(A *  B * C)

comparison = list()
for i in range(1, 10):
    comparison.append(str(i))
#print(multiple)
result = list()
for j in comparison:
    num = multiple.count(j)
   # print('num :' , num)
    result.append(num)
print(multiple.count('0'))
for m in result:
    print(int(m))
