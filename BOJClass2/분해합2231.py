N = int(input())

def generator(m: int):
    result = 0
    for i in str(m):
        result += int(i)
    return result + m

generators = list()
for i in range(1, N+1):
    a = generator(i)
    if a == N:
        generators.append(i)

if len(generators) == 0:
    print(0)
else:
    print(min(generators))

