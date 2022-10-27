def solution(bin1, bin2):
    answer = ''
    bin1 = int(bin1,2)
    bin2 = int(bin2,2)
    bin3 = bin1 + bin2
    answer += bin(bin3)[2:]
    return answer