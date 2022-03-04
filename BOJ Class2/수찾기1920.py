import sys

N = int(sys.stdin.readline())
answer = list()

number_N = list(map(int, sys.stdin.readline().rstrip().split()))
number_N.sort()
M = int(sys.stdin.readline())

number_M = list(map(int, sys.stdin.readline().rstrip().split()))

def bisect(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for num in number_M:
    result = bisect(number_N, num, 0, N-1)
    if  result == None:
        print(0)
    else:
        print(1)