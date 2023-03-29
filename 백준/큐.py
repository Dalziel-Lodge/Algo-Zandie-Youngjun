from collections import deque
import sys

n = int(input())
command = ''
queue = deque()

def push(a):
    queue.append(a)

def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[len(queue)-1])

def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)
def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        queue.popleft()

for _ in range(n):
    commands = list(sys.stdin.readline().split())
    command = commands[0]
    if command == "push":
        push(int(commands[1]))
    elif command == "front":
        front()
    elif command == "back":
        back()
    elif command == "size":
        size()
    elif command == "empty":
        empty()
    elif command == "pop":
        pop()
