def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        # print(tmp) 비트 연산자 or, 0 or 1이면 1
        tmp = tmp[2:].zfill(n)
        # print(tmp) zfill 원하는 만큼 0으로 앞에서부터 채워줌
        tmp = tmp.replace('1','#').replace('0', ' ')
        answer.append(tmp)
    return answer
