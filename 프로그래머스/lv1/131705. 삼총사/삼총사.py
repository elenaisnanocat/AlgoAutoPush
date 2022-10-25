from itertools import combinations

def solution(number):
    answer = []
    cnt = 0
    for i in combinations(number,3):
        # print(i)
        answer.append(i[0] + i[1] + i[2])
    for zero in answer:
        if zero == 0:
            cnt += 1
    return cnt