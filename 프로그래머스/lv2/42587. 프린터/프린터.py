from collections import deque

def solution(priorities, location):
    idx_pri = deque([(i,v) for i, v in enumerate(priorities)])
    answer = 0
    
    # print(idx_pri)
    while idx_pri:
        val = idx_pri.popleft()
        # print(val[1])
        if idx_pri and val[1] < max(idx_pri, key= lambda x:x[1])[1]:
            idx_pri.append(val)
        else:
            # print(val)
            answer += 1
            if val[0] == location:
                break
    return answer