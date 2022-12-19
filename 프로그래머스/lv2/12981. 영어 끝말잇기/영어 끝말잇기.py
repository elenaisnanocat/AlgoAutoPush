def solution(n, words):
    answer = [0,0]
    
    cnt = 0
    word_list = []
    word_list.append(words[0])
    
    for i in range(1, len(words)):
        cnt += 1
        if words[i] not in word_list and words[i-1][-1] == words[i][0]:
            word_list.append(words[i])
        else:
            answer[0] = cnt % n + 1
            answer[1] = cnt // n + 1
            break
            
    return answer