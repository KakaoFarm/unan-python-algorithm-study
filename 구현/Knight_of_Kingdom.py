import sys

pos = sys.stdin.readline().rstrip()

col = ['a','b','c','d','e','f','g','h']
x = col.index(pos[0]) + 1
y = int(pos[1])

'''
딕셔너리 이용방법
dic_change ={
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8
}

x = dic_change(pos[0])

'''

m1 = x + 2, y + 1
m2 = x + 2, y - 1
m3 = x - 2, y - 1
m4 = x - 2, y + 1
m5 = x + 1, y + 2
m6 = x + 1, y - 2 
m7 = x - 1, y + 2
m8 = x - 1, y - 2

data = [m1,m2,m3,m4,m5,m6,m7,m8]

count = 0
for i in data:
    if  1 <= i[0] <= 8:
        if 1<= i[1] <= 8:
            count += 1
        else:
            pass
    else:
        pass
print(count)


'''
g = input()
count = 0

dic_change = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
x,y = dic_change[g[0]],int(g[1])

move_root = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

for i in move_root:
  print(i)
  x_d = x + i[0]
  y_d = y + i[1]
  print("[chk] x_d,y_d : ",x_d,y_d)
  if x_d >= 1 and x_d <= 8 and y_d >= 1 and y_d <= 8:
    count += 1
    print("count += :",count,"\n")

print (count)

'''