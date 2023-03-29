import sys
from collections import deque



n, k = map(int, sys.stdin.readline().split())



queue = deque()
result = []

#1, 2, 3, 4, 5, 6, 7


for i in range(n):
    queue.append(i+1)


while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())


print("<", end='')
for i in result:
    if i == result[len(result)-1]:
        print(i, end='>')
    else:
        print(i, end=', ')