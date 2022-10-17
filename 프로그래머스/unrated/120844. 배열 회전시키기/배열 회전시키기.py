from collections import deque

def solution(numbers, direction):
    answer = []
    if direction == "right":
        ri = numbers.pop()
        answer.append(ri)
        answer = answer + numbers
    else:
        dn = deque(numbers)
        le = dn.popleft()
        answer += dn
        answer.append(le)
    return answer