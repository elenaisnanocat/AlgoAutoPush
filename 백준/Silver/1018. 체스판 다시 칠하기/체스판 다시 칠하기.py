N , M = map(int,input().split())
arr = list(input() for _ in range(N))
cnt = []

for i in range(N-7):
    for j in range(M-7):
        idx1  = 0 #W로 시작했을때 
        idx2 = 0
        for r in range(i,i+8):
            for c in range(j,j+8):
                if (r+c) %2 == 0: #짝수번째칸이
                    if arr[r][c] != 'W': #W가 아닐경우
                        idx1 += 1 #1개만큼 다시 칠해야 한다
                    elif arr[r][c] != 'B':
                        idx2 += 1
                else:
                    if arr[r][c] != 'B':
                        idx1 +=1 
                    elif arr[r][c] != 'W':
                        idx2 += 1
        cnt.append(min(idx1,idx2))

print(min(cnt))