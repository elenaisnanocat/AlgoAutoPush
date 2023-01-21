def solution(s):
    answer = []
    # dic = {}
    # for i in range(len(s)):
    #     if s[i] in dic:
    #         answer.append(i-dic[s[i]])
    #     else:
    #         answer.append(-1)
    #     dic[s[i]]=i
    #     for i in dic:
    #         print(i , end =" ")
    #         print(dic[i], end=" ")
    #     print()
    arr = [-1]*27
    for i in range(len(s)):
        if arr[ord(s[i])-ord('a')]>=0:
            answer.append(i-arr[ord(s[i])-ord('a')])
        else:
            answer.append(-1)
        arr[ord(s[i])-ord('a')]=i
    print(arr)
    return answer