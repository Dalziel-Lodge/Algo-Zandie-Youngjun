import sys
n = int(sys.stdin.readline().strip())
stack = []

sequence = []
for i in range(n):
    sequence.append(int(sys.stdin.readline().strip()))

index = 0

plus_minus = []


for i in range(1, n+1):
    if sequence[index] in stack:
        if stack[-1] == sequence[index]:
            stack.pop()
            index += 1
            plus_minus.append('-')
        else:
            break
    stack.append(i)
    plus_minus.append('+')
    if stack[-1] == sequence[index]:
        stack.pop()
        index += 1
        plus_minus.append('-')

print(stack)
print(plus_minus)
