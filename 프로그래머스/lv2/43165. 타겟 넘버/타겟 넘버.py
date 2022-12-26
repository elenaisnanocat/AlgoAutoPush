from collections import deque

def solution(numbers, target):
    answer = 0
    que = deque()
    
    lth = len(numbers)
    que.append([+numbers[0],0])
    que.append([-numbers[0],0])
    # print(que) 	deque([[4, 0], [-4, 0]])
    
    while que:
        temp, idx = que.popleft()
        # print(temp, idx) 4 0
        idx += 1
        if idx < lth:
            que.append([temp+numbers[idx], idx])
            que.append([temp-numbers[idx], idx])
            # print(que) deque([[-4, 0], [5, 1], [3, 1]])
            # ... deque([[8, 3], [6, 3], [4, 3], [2, 3], [6, 3], [4, 3], [2, 3], [0, 3], [0, 3], [-2, 3], [-4, 3], [-6, 3], [-2, 3], [-4, 3], [-6, 3], [-8, 3]])
        else:
            if temp == target:
                answer += 1
    return answer