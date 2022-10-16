def solution(n):
    answer = 2
    if n**0.5 == int(n**0.5):
        answer = 1
    return answer