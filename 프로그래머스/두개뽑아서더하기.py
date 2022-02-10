def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                pass
            else:
                x = numbers[j] + numbers[i]
                result.append(x)
    
    result.sort(reverse = True)
    return list(set(result))
           
