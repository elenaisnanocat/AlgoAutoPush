def solution(t, p):
#   일단 t를 p길이만큼 슬라이싱한거를 빈리스트에 더함
#   빈 리스트에 값을 크기비교함 + cnt+=1
    answer = []
    cnt = 0
    l = len(p)
    for i in range(len(t)-l+1):
        answer.append(t[i:i+l])

    for i in answer:
        if int(i) <= int(p):
            cnt += 1
    return cnt