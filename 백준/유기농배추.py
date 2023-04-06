import sys

sys.setrecursionlimit(10000)

def dfs(x,y):
    visited[x][y] = True
    directions = [(1,0), (-1,0), (0,1),(0,-1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx, ny)

t = int(sys.stdin.readline().strip())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    count = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)