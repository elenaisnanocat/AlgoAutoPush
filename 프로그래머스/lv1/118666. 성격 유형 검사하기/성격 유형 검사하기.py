def solution(survey, choices):
    answer = ''
    dic= {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0 }
    
    for s,c in zip(survey,choices):
        # print(s,c) AN 5
        if c>4:
            # print(s[1]) N
            dic[s[1]] += c-4
        elif c<4:
            # print(s[0]) C
            dic[s[0]] += 4-c
    
    lst = list(dic.items())
    # print(lst) [('R', 0), ('T', 3), ('C', 1), ('F', 0), ('J', 0), ('M', 2), ('A', 1), ('N', 1)]
    
    for i in range(0,8,2):
        if lst[i][1] < lst[i+1][1]:
            answer += lst[i+1][0]
        else:
            answer += lst[i][0]
        
    return answer