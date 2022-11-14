# from collections import deque

# N, M = map(int,input().split())
# arr = []
# for _ in range(N):
#     arr.append(list(map(int,input())))

# que = deque([(0,0)])

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# visited = [[0]*M for _ in range(N)]
# visited[0][0] = 1

# while que:
#     x, y = que.popleft()
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]

#         if 0 <= nx < N and 0 <= ny < M :
#             if visited[nx][ny] == 0 and arr[nx][ny] == 1:
#                 visited[nx][ny] = visited[x][y] + 1
#                 que.append((nx,ny))

# print(visited[N-1][M-1])
# 11/14일 통과 코드


from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

def bfs(x, y):
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
 
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      
      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
        
  return graph[N-1][M-1]

print(bfs(0, 0))
