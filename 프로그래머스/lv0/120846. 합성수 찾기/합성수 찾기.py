def solution(n):
    answer = 0
    cnt_lst = []
    for i in range(1,n+1):
        now_count = 0
        for j in range(1,i+1):
            if i % j == 0:
                now_count += 1
        cnt_lst.append(now_count)
    
    for i in cnt_lst:
        if i >= 3:
            answer+= 1
    return answer