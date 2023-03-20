from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_lst = []
    str2_lst = []
    
    for i in range(len(str1_low)-1):
        if str1_low[i].isalpha() and str1_low[i+1].isalpha():
            str1_lst.append(str1_low[i] + str1_low[i+1])
    for j in range(len(str2_low)-1):
        if str2_low[j].isalpha() and str2_low[j+1].isalpha():
            str2_lst.append(str2_low[j] + str2_low[j+1])
            
    Counter1 = Counter(str1_lst)
    Counter2 = Counter(str2_lst)
    # print(Counter1, Counter2)
    
    inter = list((Counter1 & Counter2).elements()) #Counter elements() 메서드 사용하면 카운터 된 숫자만큼 요소 리턴
    # print(Counter1 & Counter2) Counter({'ha': 2, 'an': 1, 'nd': 1, 'ds': 1, 'sh': 1, 'ak': 1, 'ke': 1})
    # print(inter) ['ha', 'ha', 'an', 'nd', 'ds', 'sh', 'ak', 'ke']
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)