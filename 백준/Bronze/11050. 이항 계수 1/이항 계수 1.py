def factorial(n):
    ans = 1
    for i in range(2,n+1):
        ans*=i
    return ans

def combination(n,k):
    return factorial(n)//factorial(n-k)//factorial(k)

n,k = map(int,input().split())
result = combination(n,k)
print(result)