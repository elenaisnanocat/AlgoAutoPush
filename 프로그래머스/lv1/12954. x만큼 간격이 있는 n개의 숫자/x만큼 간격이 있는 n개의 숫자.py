def solution(x, n):
    answer = []
    for i in range(n):
        next = x+x*i
        answer.append(next)
    return answer