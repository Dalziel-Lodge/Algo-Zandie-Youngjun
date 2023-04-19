import sys
from collections import deque

n, m = map(int, input().split())

miro = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    string = input().strip()
    line = []
    for j in string:
        line.append(int(j))
    miro.append(line)

def bfs(visited):
    queue = deque([[[0, 0], 1]])
    visited[0][0] = True
    while queue:
        pos, dist = queue.popleft()
        x, y = pos #따로 담는게 직관적이다

        if x == n - 1 and y == m - 1: #탈출조건 명시
            return dist

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #상하좌우 좌표로 표현하기
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and miro[nx][ny]:
                queue.append([[nx, ny], dist + 1])
                visited[nx][ny] = True

    return -1 #못찾았을 때인데 호출안됨

result = bfs(visited)
print(result)
