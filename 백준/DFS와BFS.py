import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        newv = queue.popleft()
        print(newv, end = ' ')
        for i in graph[newv]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, sys.stdin.readline().split())

visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(graph, v, visited)
print("")

visited = [False]*(n+1)
bfs(graph, v, visited)