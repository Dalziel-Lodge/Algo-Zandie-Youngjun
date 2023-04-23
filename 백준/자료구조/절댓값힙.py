import sys
import heapq

n = int(sys.stdin.readline().strip())

queue = []
minus_queue = []

for i in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if len(queue) == 0 and len(minus_queue) == 0:
            print(0)
        elif len(queue) == 0:
            print(-heapq.heappop(minus_queue))
        elif len(minus_queue) == 0:
            print(heapq.heappop(queue))
        else:
            a = heapq.heappop(queue)
            b = heapq.heappop(minus_queue)
            if a < b:
                print(a)
                heapq.heappush(minus_queue, b)
            else:
                print(-b)
                heapq.heappush(queue, a)
    else:
        if num > 0:
            heapq.heappush(queue, num)
        else:
            heapq.heappush(minus_queue, -num)
            #부호가 바껴서 +지만 -라고 생각하기
