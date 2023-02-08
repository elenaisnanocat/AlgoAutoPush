def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        # if s[0] == ')':
        #     return False
        if s[i] == '(':
            stack.append(s[i])
        # elif s[i] == ')' and stack[-1] == '(':
        #     stack.pop()
        else:
            if s[0] == ')':
                return False
            elif len(stack) != 0 and stack[-1] == '(':
                stack.pop()
        
    if len(stack) == 0:
        answer = True
    else:
        answer = False
    return answer