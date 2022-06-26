t = int(input())

for _ in range(t):  
    floor = int(input())  
    num = int(input()) 
    f0 = [x for x in range(1, num+1)]  # 0층 리스트
    for k in range(floor):  
        for i in range(1, num):  
            f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f0[-1])