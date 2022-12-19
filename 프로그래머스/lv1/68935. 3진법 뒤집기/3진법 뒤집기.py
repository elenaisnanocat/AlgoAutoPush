def solution(n):
    answer = ''
    while n>0:
        n, re = divmod(n,3)
        answer += str(re)
        # print(answer)
    answer = int(answer,3)    
    return answer