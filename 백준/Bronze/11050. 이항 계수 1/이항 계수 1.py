from itertools import combinations

N,K = map(int,input().split())
com = list(combinations(range(N),K))
print(len(com))