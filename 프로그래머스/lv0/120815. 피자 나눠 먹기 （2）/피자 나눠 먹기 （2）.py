import math

def solution(n):
    answer = 0
    pizzabox = 6
    
    while pizzabox % n != 0:
        pizzabox += 6
    return pizzabox // 6