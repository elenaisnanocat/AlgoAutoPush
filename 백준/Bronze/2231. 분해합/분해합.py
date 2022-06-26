N = int(input())
result = 0
for i in range(1,N+1):
    a= list(map(int,str(i)))
    result = i+sum(a)
    if result == N:
        print(i)
        break
    if i == N:
        print(0)