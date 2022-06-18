import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    word = input().split()
    order = word[0]

    if 'push' in word:
        value = word[1]
        stack.append(value)
    elif 'pop' in word:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in word:
        print(len(stack))
    elif 'empty' in word:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in word:
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)