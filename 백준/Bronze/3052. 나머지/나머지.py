T = 10
num_list = []
for _ in range(1,T+1):
    num = int(input())
    last = num % 42
    num_list.append(last)

result = set(num_list)
print(len(result))