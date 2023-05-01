def solution(files):
    answer = []
    for file in files:
        head, num, tail = '', '', ''
        num_chk = 0
        for i in range(len(file)):
            if file[i].isdigit():
                num += file[i]
                num_chk = 1
            elif num_chk != 1:
                head += file[i]
            else:
                tail = file[i:]
                break
        answer.append((head, num, tail))
    answer.sort(key=lambda x : (x[0].upper(), int(x[1])))
    return [''.join(t) for t in answer]