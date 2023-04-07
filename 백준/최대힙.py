import sys
import heapq

heap = []

n = int(sys.stdin.readline().strip())
for i in range(n):
    a = int(sys.stdin.readline().strip())
    if heap and a == 0:
        print(-heapq.heappop(heap))
    elif not heap and a == 0:
        print(0)
    else:
        heapq.heappush(heap, -a)