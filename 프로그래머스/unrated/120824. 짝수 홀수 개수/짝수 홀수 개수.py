def solution(num_list):
    answer = []
    
    cnt = 0
    odd = 0
    for i in num_list:
        if i % 2 == 0:
            cnt += 1
        else:
            odd += 1
    
    return [cnt,odd]