import sys

n = int(input())
command = ''
stack = []

def push(a):
    stack.append(a)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack)-1])

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[len(stack)-1])
        stack.pop(-1)

for _ in range(n):
    commands = list(sys.stdin.readline().split())
    command = commands[0]
    if command == "push":
        push(int(commands[1]))
    elif command == "top":
        top()
    elif command == "size":
        size()
    elif command == "empty":
        empty()
    elif command == "pop":
        pop()

