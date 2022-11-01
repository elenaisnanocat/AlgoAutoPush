def solution(price):
    answer = 0
    if 100000 <= price < 300000:
        price -= price*0.05
    elif 300000 <= price < 500000:
        price -= price*0.1
    elif 500000 <= price:
        price -= price * 0.2
    else:
        price = price
    answer = int(price)
    
    return answer