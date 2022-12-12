def solution(new_id):
    answer = ''
    # state 1
    new_id = new_id.lower()
    # state 2
    for w in new_id:
        if w.isalpha() or w.isdigit() or w in ['-', '_', '.']:
            answer += w
    # state 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # state 4
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:] 
        else:
            answer = '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # state 5
    if answer == '':
        answer = 'a'
    # state 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # state 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer