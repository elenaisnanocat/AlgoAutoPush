def solution(numbers):
    total = 0
    
    for i in range(len(numbers)-1):
        if total < numbers[i] * numbers[i+1]:
            total = numbers[i] * numbers[i+1]
            
    return total