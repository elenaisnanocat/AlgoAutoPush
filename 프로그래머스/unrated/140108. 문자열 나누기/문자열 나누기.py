def solution(s):
    answer = 0
    x_cnt = 0
    n_cnt = 0
    x = ""
    for i in range(len(s)):
        if x == "":
            x=s[i]
            x_cnt +=1
        elif x == s[i]:
            x_cnt += 1
        else:
            n_cnt += 1
        if x_cnt == n_cnt:
            answer+=1
            x = ""
            x_cnt = 0
            n_cnt = 0
    if x != "":
        answer +=1
    return answer