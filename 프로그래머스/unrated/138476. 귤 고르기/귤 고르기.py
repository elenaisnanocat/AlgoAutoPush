from collections import Counter

def solution(k, tangerine):
    answer = 0
    # c= Counter(tangerine).items()
    # print(c) dict_items([(1, 1), (3, 2), (2, 2), (5, 2), (4, 1)]) 크기, 갯수
    count = sorted(Counter(tangerine).items(),key = lambda x : x[1],reverse = True)

    for key, value in count:
        if k <= 0: 
            break
        k -= value
        answer += 1
    return answer