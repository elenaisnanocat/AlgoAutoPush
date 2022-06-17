import sys
input = sys.stdin.readline

def binary(i):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end) // 2
        if n_lst[mid] == i:
            return True
        if i < n_lst[mid]:
            end = mid - 1
        elif i > n_lst[mid]:
            start = mid + 1



n = int(input())
n_lst = list(map(int,input().split()))
n_lst.sort()

m = int(input())
m_lst = list(map(int,input().split()))

for i in range(m):
    if binary(m_lst[i]):
        print(1)
    else:
        print(0)