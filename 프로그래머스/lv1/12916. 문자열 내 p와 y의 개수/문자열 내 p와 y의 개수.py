def solution(s):
    answer = True
    
    cntp = s.count('p') + s.count('P')
    cnty = s.count('y') + s.count('Y')
    
    if cntp != cnty:
        answer = False
        
    return answer