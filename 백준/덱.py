from collections import deque
import sys

n = int(input())
command = ''
queue = deque()

def push_front(a):
    queue.appendleft(a)

def push_back(a):
    queue.append(a)

def pop_front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        queue.popleft()

def pop_back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[len(queue)-1])
        queue.pop()

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)


def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[len(queue)-1])

for _ in range(n):
    commands = list(sys.stdin.readline().split())
    command = commands[0]
    if command == "push_front":
        push_front(int(commands[1]))
    elif command == "push_back":
        push_back(int(commands[1]))
    elif command == "front":
        front()
    elif command == "back":
        back()
    elif command == "size":
        size()
    elif command == "empty":
        empty()
    elif command == "pop_front":
        pop_front()
    elif command == "pop_back":
        pop_back()
