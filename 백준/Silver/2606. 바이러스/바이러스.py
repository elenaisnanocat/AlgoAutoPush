n = int(input())		
m = int(input())		

arr = [[] for _ in range(n+1)]
for _ in range(m):							
    x, y = map(int, input().split())		
    arr[x].append(y)
    arr[y].append(x)

visited = [0] * (n+1)	

def dfs(arr, v, visited):
    visited[v] = 1
    for i in arr[v]:
        if visited[i] == 0:
            dfs(arr, i, visited)
    return True

dfs(arr, 1, visited)
print(sum(visited)-1)