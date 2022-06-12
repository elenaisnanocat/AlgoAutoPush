h,m = map(int,input().split())

if h>=1 and m-45<0:
    print(h-1,m-45+60)
elif m>=45:
    print(h,m-45)
else:
    print(23,m+15)