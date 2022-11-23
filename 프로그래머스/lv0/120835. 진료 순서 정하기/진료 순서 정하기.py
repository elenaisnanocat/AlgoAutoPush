def solution(emergency):
    answer = []
    dict = {num: index for index, num in enumerate(sorted(emergency, reverse=True), start=1)}
    for i in emergency:
        answer.append(dict[i])
    return answer