def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        s = ""
        for w in skill_tree:
            if w in skill:         
                s += w
        
        if skill[:len(s)] == s:
            #print(skill[:len(s)]) CB
            answer += 1
    
    return answer