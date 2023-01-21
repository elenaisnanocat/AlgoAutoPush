def solution(today, terms, privacies):
    answer = []
    alpha = {}
    print(today, terms, privacies)
    print(privacies)
    
    for k in today:
        y,m,d = today.split('.')
    to = y + m + d
    print(to)
    
    for i in terms:
        a = i.split()
        alpha[a[0]]=int(a[1])
        print(alpha)
        
    for j in range(len(privacies)):
        # nowday, nowpri = j.split()
        nowday, nowpri = privacies[j].split()
        print(nowday, nowpri)
        
        print(alpha[nowpri])
        YYYY,MM,DD = map(int,nowday.split('.'))
        print(YYYY,MM,DD)
        MM += alpha[nowpri]
        if MM % 12 == 0:
            YYYY += MM//12 - 1
            MM = 12
        else:
            YYYY += MM//12
            MM -= MM//12*12
        # if MM + alpha[nowpri] > 12:
        #     MM = MM + alpha[nowpri] - 12
        #     YYYY = YYYY + 1
        # else:
        #     MM = MM + alpha[nowpri]
        if DD != 1:
            DD -= 1
        else:
            DD = 28
            MM -= 1
            if MM == 0:
                YYYY-=1
                MM = 12
        print(YYYY, MM, DD)
        if MM < 10:
            MM = "0" + str(MM)
        if DD < 10:
            DD = "0" + str(DD)
        pri = str(YYYY) + str(MM) + str(DD)
        print(pri)
        print(to)
        print(int(pri)-int(to))
        if int(pri)<int(to):
            answer.append(j+1)    

    return answer