from collections import Counter

def solution(spell, dic):
    answer = 0
    for i in dic:
        # print(Counter(spell))
        # print(Counter(dic))
        # print(Counter(i))
        # print(Counter(spell)-Counter(i))
        if len(Counter(spell)-Counter(i)) == 0:
            answer = 1
            break
        else:
            answer = 2
    return answer

