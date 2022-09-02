def solution(n):
    answer = []
    num = reversed(str(n))
    for i in num:
        answer.append(int(i))
    return answer