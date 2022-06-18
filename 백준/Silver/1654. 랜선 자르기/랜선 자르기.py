import sys
k,n = map(int,input().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]

start = 1
end = max(lan)

while start <= end:
    cnt = 0
    mid = (start+end)//2
    for i in lan:
        cnt += i//mid #중간값으로 자른 갯수
    if cnt >= n:
        start = mid+1
    else:
        end = mid -1
print(end)