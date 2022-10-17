def solution(my_string):
    answer = 0
    for i in my_string:
        if ord('1') <= ord(i) <= ord('9'):
            answer += int(i)
    return answer