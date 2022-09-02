def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    ans = int(''.join(answer))
    return ans