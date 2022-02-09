
N = int(input())
p = []
for i in range(N):
    S = input()
    p.append(S)

q = p[0]
x = ','.join(q).split(',')

for i in range(len(p[0])):
    for j in range(len(p)):
        if p[0][i] == p[j][i]:
            pass
        else:
            x[i] = "?"
            

print(''.join(x))