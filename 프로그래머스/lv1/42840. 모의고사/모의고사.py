def solution(answers):
    answer = []
    
    score = [0, 0, 0]
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == stu1[i%5]:
            score[0] += 1
        if answers[i] == stu2[i%8]:
            score[1] += 1
        if answers[i] == stu3[i%10]:
            score[2] += 1
    
    for i, stu in enumerate(score):
        # print(i,stu)
        if stu == max(score):
            answer.append(i+1)
    return answer