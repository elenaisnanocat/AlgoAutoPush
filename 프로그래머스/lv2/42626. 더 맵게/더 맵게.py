# from collections import deque
# 시간초과...-1
# def solution(scoville, K):
    # answer = []
    # cnt = 0
    # print(scoville)
    # for j in range(len(scoville)):
    #     if scoville[0] < K:
    #         scoville = deque(scoville)
    #         fir_not =scoville.popleft()
    #         # print(scoville)
    #         answer.append(fir_not)
    #         sec_not = scoville.popleft()
    #         answer.append(sec_not)
    #         sec = fir_not +(scoville[0] * 2)
    #         scoville.popleft()
    #         scoville.appendleft(sec)
    #         scoville = list(scoville)
    #         scoville.sort()
    #         cnt += 1
#                 print(fir_not)
#                 print(sec)
#                 print(scoville)

#     print(cnt)
    # return cnt
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #리스트를 힙으로 바꿔줌
    
    while scoville[0] < K:
        if len(scoville) > 1:
            fir_not = heapq.heappop(scoville) #가장 작은 인덱스 삭제, 리턴
            # print(fir_not)
            sec_not = heapq.heappop(scoville) 
            heapq.heappush(scoville, fir_not + sec_not *2) #가장 작은 인덱스가 0으로 감.
            answer += 1
        else:
            return -1
    return answer
    
    