import sys
    
numbers = sys.stdin.readlines()

for num in numbers[:-1]:
    data = list(map(int, num.split()))
    print(data[0] + data[1])
