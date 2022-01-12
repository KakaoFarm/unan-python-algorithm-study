import sys
import operator

N = int(sys.stdin.readline())

mark_dict = {}

for i in range(N):
    marks, name = sys.stdin.readline().rstrip().split()
    mark_dict[marks] = name

# s_dict= sorted(mark_dict.items(), key=operator.itemgetter(0))
s_dict = sorted(mark_dict)
for i in s_dict:
    print(i[0], end = " ")




    