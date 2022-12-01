import sys

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None   

if __name__ == '__main__':

    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))

    M = int(sys.stdin.readline())
    req = list(map(int, sys.stdin.readline().split()))

    array.sort()
    
    for target in req:
        result = binary_search(array, target, 0, N-1)
    
        if result != None:
            print("yes", end=' ')
        else:
            print("no", end = ' ')
    




