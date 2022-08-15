import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
seq = [1,1,1,2,2]

for i in range(5, max(arr)):
    seq.append(seq[i-1]+seq[i-5])

for pn in arr:
    print(seq[pn-1]) 