def check(x,row):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i: #같은 열, 대각선
            return False
    return True

def dfs(x,n,row):
    global result
    
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i #몇번째줄 i번째 인덱스
            if check(x,row): #가로세로대각선 있는지 확인
                dfs(x+1,n,row)
    return result

def solution(n):
    row = [0]*n
    global result
    
    result = 0
    dfs(0,n,row)
    
    return result