def solution(array):
    answer = 0
    array.sort()
    num = len(array) // 2 
    for i in range(len(array)):
        if i == num:
            answer = array[i]
    return answer