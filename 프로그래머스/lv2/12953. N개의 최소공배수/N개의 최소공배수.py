import math

def LCM(a,b):
    return a * b // math.gcd(a,b)

def solution(arr):
    arr.sort()
    temp = arr[0]
    for i in range(0, len(arr)-1):
        temp = LCM(temp, arr[i+1])
    return temp
    