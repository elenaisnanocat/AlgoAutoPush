from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    que.append([x, y])
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
                que.append([nx, ny])
                visited[nx][ny] = 1

n = int(input())
arr = [list(input()) for _ in range(n)]
que = deque()
visited = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1
print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1
print(cnt)