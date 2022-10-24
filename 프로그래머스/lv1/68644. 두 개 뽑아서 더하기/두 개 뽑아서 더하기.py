from itertools import combinations

def solution(numbers):
    answer = []
    com_lst = list(combinations(numbers,2))
    # print(com_lst)
    for i in com_lst:
        answer.append(i[0]+i[1])
    answer.sort()
    print(answer)
    answer = list(set(answer))
    print(answer)
    return sorted(answer)