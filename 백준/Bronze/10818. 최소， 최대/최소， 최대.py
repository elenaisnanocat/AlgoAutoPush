n = int(input())
lst = list(map(int,input().split()))

max_v = lst[0]
min_v = lst[0]
for i in range(n):
    if lst[i] > max_v:
        max_v = lst[i]
    if lst[i] < min_v:
        min_v = lst[i]

print(f'{min_v} {max_v}')
