import time

array = [7,5,9,0,3,1,6,2,4,8]

start_time = time.time()

for i in range(1, len(array)):
    for j in range(i, 0 ,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            print(array)
        
        else:
            break

end_time = time.time()

print(end_time - start_time)
print(array)