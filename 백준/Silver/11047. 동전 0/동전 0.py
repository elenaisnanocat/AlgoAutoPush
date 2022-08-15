n,k = map(int,input().split())

coins = [int(input()) for _ in range(n)]
# print(coins)
coins.sort(reverse=True)

ans = 0
for coin in coins:
    if k >= coin:
        ans += k // coin
        k = k % coin
        if k <= 0 :
            break
print(ans)
