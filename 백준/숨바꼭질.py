import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

#0~100000까지니까 100001개 만들어야함
visited = [False] * 100001
time = 0

def bfs(visited, n, k):
    queue = deque([(n,0)])
    visited[n] = True
    while queue:
        #큐에서 꺼내서 curr, time에 저장
        curr, time = queue.popleft()
        #현재 위치가 k이면 time 리턴
        if curr == k:
            return time
        for next_pos in [curr-1, curr+1, curr*2]:
            #다음 위치가 수직선 범위 내이고, 방문한 적 없다면
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                #큐에 해당 위치를 추가
                queue.append((next_pos, time+1))
                #방문처리
                visited[next_pos] = True

print(bfs(visited, n, k))