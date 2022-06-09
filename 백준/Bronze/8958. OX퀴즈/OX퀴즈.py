n = int(input())
for _ in range(1,n+1):
    while True:
        try:
            arr = list(input())
            cnt = 0
            result = 0
            for i in range(len(arr)):
                if arr[i] == 'O':
                    cnt += 1
                    result += cnt
                else:
                    cnt = 0
            print(result)
        except:
            break