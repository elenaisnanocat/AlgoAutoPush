T= int(input())
for tc in range(T):
    r,s = input().split()
    S = str(s)
    r = int(r)

    for i in range(len(S)):
        ans = S[i] * r
        print(ans,end='')
    print()