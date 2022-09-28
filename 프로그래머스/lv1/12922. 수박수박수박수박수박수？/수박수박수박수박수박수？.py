def solution(n):
    answer = '수박'
    ans = answer*(n//2)+answer[:n%2]
          
    return ans