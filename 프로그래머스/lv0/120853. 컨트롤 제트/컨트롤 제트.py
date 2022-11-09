def solution(s):
    answer = []
    total = 0
    s = s.split()
    
    for i in s:
        if i != 'Z':
            answer.append(i)
        elif i == 'Z' and len(answer) !=0 : 
            answer.pop()
    
    for i in answer:
        total += int(i)
    
    return total