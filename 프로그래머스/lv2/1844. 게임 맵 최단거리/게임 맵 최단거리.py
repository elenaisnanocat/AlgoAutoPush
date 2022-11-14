from collections import deque

def solution(maps):
    answer = 0
    
    
    visited = [[-1]*len(maps[0]) for _ in range(len(maps))]
    que = deque()
    que.append((0,0))
    visited[0][0] = 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while que:
        x, y = que.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx,ny))
    
    return visited[len(maps)-1][len(maps[0])-1]