def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        for num_str in str(num):
            if int(num_str) == k:
                answer += 1
    return answer