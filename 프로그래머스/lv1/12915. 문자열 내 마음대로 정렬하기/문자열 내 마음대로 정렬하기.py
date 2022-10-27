def solution(strings, n):

    c = sorted(strings, key = lambda x : (x[n],x))
     # (x[n],x) x[n] 기준으로 정렬하고, x로 문자열 사전순으로 정렬
    return c