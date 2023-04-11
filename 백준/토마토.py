import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomatoes = []

for _ in range(n):
    tomatoes.append(list(map(int, sys.stdin.readline().split())))

# 익은 토마토 위치를 모두 큐에 추가합니다.
queue = deque()
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 1:
            queue.append((i, j, 0))

# BFS
day = 0
while queue:
    a, b, day = queue.popleft()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        na = a + dx
        nb = b + dy
        if 0 <= na < n and 0 <= nb < m and tomatoes[na][nb] == 0:
            tomatoes[na][nb] = 1
            queue.append((na, nb, day+1))

# 토마토가 모두 익었는지 확인
for i in range(n):
    for j in range(m):
        if tomatoes[i][j] == 0:
            print(-1)
            exit()

# 모든 토마토가 익은 경우, 최소 일수를 출력
print(day)