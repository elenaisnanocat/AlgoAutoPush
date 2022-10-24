def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)
    print(citations)
    for i , c in enumerate(citations):
        print(i,c)
        if i >= c:
            return i
            print(i)
    return answer