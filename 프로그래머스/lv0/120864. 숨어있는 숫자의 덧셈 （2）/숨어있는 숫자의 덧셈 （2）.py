import re

def solution(my_string):
    answer = 0
    numbers = re.findall(r'\d+', my_string)
    # print(numbers)
    for i in numbers:
        answer += int(i)
    return answer