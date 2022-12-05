from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n
    # print(check)
    
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        # print(c)
        if c == check:
            answer += 1

    return answer