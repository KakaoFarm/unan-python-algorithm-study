points = {}
for i in range(8):
    point = int(input())
    points[i+1] = point
a = sorted(points.items(), key = lambda x: x[1], reverse=True)

total_points = 0
quiz_order = []
for i in a[:5]:
    total_points += i[1]
    quiz_order.append(i[0])

quiz_order.sort()
print(total_points)
for i in quiz_order:
    print(i, end = " ")