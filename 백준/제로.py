import sys

k = int(sys.stdin.readline().strip())

stack = []

for _ in range(k):
    number = int(sys.stdin.readline().strip())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))