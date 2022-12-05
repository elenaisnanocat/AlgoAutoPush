def solution(id_list, report, k):
    
    report = set(report)
    answer = {x:0 for x in id_list}
    # print(answer)
    reports = {x:0 for x in id_list}
    
    for x in report:
    
        reports[x.split()[1]] += 1
        # print(reports)
    
    for x in report:
        if reports[x.split()[1]] >= k:
            answer[x.split()[0]] += 1
    
    # print(answer.values())
    return list(answer.values())