def check(idx, row): #세로대각선체크
    for i in range(idx):
        if row[idx] == row[i] or abs(row[idx]-row[i]) == idx - i:
            return False
    return True

def dfs(idx, n, row):
    global result

    if idx == n:
        result += 1
    else:
        for i in range(n):
            row[idx] = i
            if check(idx,row):
                dfs(idx+1, n, row)

n = int(input())
row = [0]*n
result = 0
dfs(0, n, row) #(n, row안써도 된다함..)
print(result)