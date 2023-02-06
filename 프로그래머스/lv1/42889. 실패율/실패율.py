def solution(N, stages):
    answer = []
    stage = [0] * N
    
    failrate = []
    for i in range(len(stages)):
        if stages[i] <= N:
            stage[stages[i]-1] += 1
            # print(stage) [1, 3, 2, 1, 0]
        else:
            continue
    
    for i in range(len(stage)):
        if stage[i] == 0:
            failrate.append([i+1,0])
        else:
            fail = stage[i] / (len(stages) - sum(stage[:i]))
            failrate.append([i+1,fail])
    
    for idx, rate in enumerate(failrate):
        c = sorted(failrate, key=lambda x: x[1],reverse=True) 
        #[[3, 0.5], [4, 0.5], [2, 0.42857142857142855], [1, 0.125], [5, 0.0]]
        
    for i in c:
        answer.append(i[0])

    return answer