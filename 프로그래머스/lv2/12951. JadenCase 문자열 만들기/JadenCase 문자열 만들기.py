def solution(s):
    answer = ''
    s = s.split(' ')
    
    for i in range(len(s)):
        # print(s)
        s[i] = s[i].capitalize()
    return ' '.join(s)