from itertools import combinations

def solution(numbers):
    lst = []
    for i in combinations(numbers,2):
        lst.append(i[0] * i[1])
    return max(lst)