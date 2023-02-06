from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n **(1/2)) + 1):
        if n % i==0:
            return False
    return True

def solution(numbers):
    answer = set()
    num_lst = []
    
    for i in numbers:
        num_lst.append(i)
        
    for i in range(1,len(num_lst)+1):
        arr = list(map(''.join, permutations(num_lst,i)))
        # print(arr)
        for j in arr:
            if is_prime(int(j)):
                answer.add(int(j))     
    return len(answer)