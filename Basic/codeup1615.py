# Self Number 
import sys
a, b = map(int,sys.stdin.readline().rstrip().split())

def generator(n :int):
    result = 0
    x = []
    for i in str(n):
        x.append(i)
    
    for j in x:
        result += int(j)
    
    result += n
    return result

def self_number(x,y):
    numbers = []
    for i in range(x,y+1,1):
        numbers.append(i)
    
    # print("numbers = ", numbers)
    
    for j in range(y):
        if generator(j) in numbers:
            # print("generator = ", generator(j))
            numbers.remove(generator(j))
            
    result = 0
    for i in numbers:
        result += int(i)
    
    return print(result)

self_number(a,b)