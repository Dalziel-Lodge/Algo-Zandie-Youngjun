#정수 N, M
#N개줄에 M개의 정수 0 or 1
#시작 마지막 1
from collections import deque

def bfs(x, y):

    #큐생성
    queue = deque()
    queue.append((x, y))
    #큐가 빌 때까지
    while queue:
        #큐에서 꺼내서 x, y 에 담기
        x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
    return graph[n -1][m -1]


n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))
