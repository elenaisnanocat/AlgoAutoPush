def solution(my_string, letter):

    str = ''
    for i in my_string:
        if i not in letter:
            str +=i
            
    return ''.join(str)