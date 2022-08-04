def solution(x):
    answer = True
    strin = str(x)

    num = 0
    for i in range(len(strin)):
        num += int(strin[i])
    
    if x % num == 0:
        answer = True
    else:
        answer = False
        
    return answer