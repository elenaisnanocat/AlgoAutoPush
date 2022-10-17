def solution(s):
    answer = []
    lst = s.split(" ")
    for i in lst:
        answer.append(int(i))
    return f'{min(answer)} {max(answer)}'