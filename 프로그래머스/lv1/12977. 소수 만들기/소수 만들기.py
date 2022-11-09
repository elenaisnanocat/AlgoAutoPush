from itertools import combinations #조합

#소수 만드는 함수
def is_prime_number(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = []
    total = []
    result = []
    
    for i in combinations(nums,3):
        answer.append(i)
    
    for ans in answer:
        total.append(sum(ans))
    # print(total)
    
    for re in total:
        if is_prime_number(re) == True:
            result.append(re)
    # print(result)
    return len(result)