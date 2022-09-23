from math import sqrt

def solution(n):
    if int(sqrt(n)) == sqrt(n):
        return (sqrt(n) + 1)*(sqrt(n) + 1)
    else:
        return -1
        
   