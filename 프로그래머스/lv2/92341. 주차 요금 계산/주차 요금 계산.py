# 차량 번호가 작은 자동차부터 주차요금
import math

def solution(fees, records):
    answer = []
    dic = dict()
    
    time, fee, utime, ufee = fees
#     주차요금 = 기본요금 + [(누적 주차 시간 - 기본시간)/단위 시간](올림) * 단위요금
    # print(time, fee, utime, ufee)
    
    for i in records:
        rtime, carnum, his = i.split()
        # print(rtime, carnum, his)
        h, m = map(int,rtime.split(':'))
        # print(h,m)
        rtime_to_min = h*60 + m
        carnum = int(carnum)
        
        if carnum in dic:
            dic[carnum].append([rtime_to_min, his])
        else:
            dic[carnum] = [[rtime_to_min, his]]
#             carnum 키값이 dic에 없음. carnum를 키값,[rtime_to_min, his]를 value로 가지는 값을 dic에 추가함
    # print(dic)
    carnum_lst = sorted(dic.items())
#     차 번호인 key값 기준으로 딕셔너리 정렬, sorted써서 리스트로 반환.
    # print(carnum_lst)
    
    for record in carnum_lst:
        t = 0
        # print(record)
        for mininout in record[1]:
            # print(mininout)
            if mininout[1] == "OUT":
                t += mininout[0]
            else:
                t -= mininout[0]
#                 출차시간 - 입차시간
#          제일 끝 기록이 IN이면
        if record[1][-1][1] == "IN":
            t += (23 * 60) + 59
#         시간 계산한게 기본시간보다 작거나 같으면
        if t <= time:
            answer.append(fee)
        else:
            answer.append(fee + math.ceil((t-time) / utime) * ufee)
            
    return answer