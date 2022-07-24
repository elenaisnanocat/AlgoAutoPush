import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = [input().strip() for i in range(N)]
M_list = [input().strip() for i in range(M)]

# 교차하는 이름들을 찾는다
duplicate = list(set(N_list) & set(M_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)