def solution(money):
    answer = []
    num = money // 5500
    left = money - 5500 * num
    answer.append(num)
    answer.append(left)
    return answer