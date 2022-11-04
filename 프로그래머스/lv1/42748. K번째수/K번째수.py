def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # print(i,j,k)
        sli = array[i-1:j]
        sli.sort()
        answer.append(sli[k-1])
    return answer