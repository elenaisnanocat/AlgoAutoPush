def solution(num, k):
    answer = 0
    num = str(num)
    k = str(k)
    if num.find(k) != -1:
        answer += num.find(k)+1
    else:
        answer += num.find(k)
    return answer