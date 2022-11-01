def solution(hp):
    answer = 0
    while hp > 0:
        if hp >= 5:
            fiv = hp // 5
            hp -= 5 * fiv
            answer += fiv
        elif hp >= 3:
            th = hp // 3
            hp -= 3 * th
            answer += th
        elif hp >= 1:
            one = hp // 1
            hp -= 1 * one
            answer += one
    return answer