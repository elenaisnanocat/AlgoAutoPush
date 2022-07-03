N = int(input())
M = int(input())

if M != 0: #고장난 버튼이 있으면 input받음
    broken_button = [int(x) for x in input().split()]
else:
    broken_button = []

result = abs(100 - N) #100에서 이동한게 최소일 수 있으므로 기본값으로 잡음

for num in range(1000001):
    n = [int(x) for x in list(str(num))]

    for i in range(len(n)):
        if n[i] in broken_button:
            break

        if i == len(n) - 1:
            count = len(n) + abs(N - num) #리모컨 누른 횟수 + 몇번 더 +나 -눌러야하는지 합산
            result = min(result, count) #둘 중 최솟값
print(result)