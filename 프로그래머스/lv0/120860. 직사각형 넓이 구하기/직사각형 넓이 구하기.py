def solution(dots):
    answer = 0
    x = []
    y = []
    
    for i in dots:
        x.append(i[0])
        y.append(i[1])
    # print(x)
    # print(y)
    x = abs(x[0]-x[1]) or abs(x[0]-x[2])
    y = abs(y[0]-y[1]) or abs(y[0]-y[2])
    answer += x * y
    return answer