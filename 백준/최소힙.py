import sys
from queue import PriorityQueue

n = int(sys.stdin.readline().strip())
que = PriorityQueue()

for i in range(n):
    a = int(sys.stdin.readline().strip())
    if not que.empty() and a == 0:
        print(que.get())
    elif que.empty() and a == 0:
        print(0)
    else:
        que.put(a)
