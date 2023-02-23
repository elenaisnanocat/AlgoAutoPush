import sys
input = sys.stdin.readline

def dfs(x):
    stack = []
    visited = [False] * (N+1)
    stack.append(x)
    visited[x] = True

    # dfs
    while stack:
        value = stack.pop()
        llst[x] += 1

        length = len(lst[value])
        for j in range(length):
            if not visited[lst[value][j]]:
                stack.append(lst[value][j])
                visited[lst[value][j]] = True

N, M = map(int,input().split())
lst = [list() for _ in range(N+1)]
temp = [list() for _ in range(N+1)] #비어있는 리스트 찾음
visited = [0]*(N+1)

for _  in range(M):
    a,b = map(int,input().split())
    lst[b].append(a)
    temp[a].append(b)
llst = [0] * (N+1)
for i in range(1,N+1):
    dfs(i)
        
a = max(llst)
# print(lst) #리프노드
# print(temp) #신뢰 받는 최상단노드 템프에서 빈 배열애들을 골라서 돌리면 된다
for j in range(len(llst)):
    if llst[j] == a:
        print(j, end= " ")