def solution(my_string):
    low = my_string.lower()
    lst = list(low)
    lst.sort()
    return ''.join(lst)