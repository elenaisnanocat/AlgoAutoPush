def rotate(A):
    return A[-1]+A[:-1]

def solution(A, B):
    answer = -1
    for i in range(len(A)):
        if i == 0 and A == B:
            answer = 0
            break
        A = rotate(A)
        
        if A == B:
            answer = i+1
            print(i)
            break
        
    return answer