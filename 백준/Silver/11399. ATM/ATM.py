import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

lst.sort()
ans = 0
for i in range(1, n+1):
    ans += sum(lst[:i])

print(ans)