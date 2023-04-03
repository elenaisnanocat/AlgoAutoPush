def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    ini = s // n
    for _ in range(n):
        answer.append(ini)
    
    idx = len(answer) - 1
    
    for _ in range(s % n): #s를 n으로 나눈 몫에서 나머지만큼 각 값에 1씩 더해줌.
        answer[idx] += 1
        idx -= 1
    return answer