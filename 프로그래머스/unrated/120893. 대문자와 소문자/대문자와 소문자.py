def solution(my_string):
    answer = ''
    print(ord('a'))
    for i in my_string:
        if ord(i) >= ord('a'):
            answer += i.upper()
        else:
            answer += i.lower()
    
    return answer