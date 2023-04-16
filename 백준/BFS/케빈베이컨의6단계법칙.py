from collections import deque

# 입력 받기
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 유저의 케빈 베이컨의 수 구하기
kevin_bacon = [0] * (N+1)
for i in range(1, N+1):
    queue = deque([(i, 0)])
    visited = [False] * (N + 1)
    visited[i] = True
    while queue:
        v, d = queue.popleft()
        kevin_bacon[i] += d
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                queue.append((u, d+1))

# 케빈 베이컨의 수가 가장 작은 사람 찾기
min_kevin_bacon = float('inf')
min_idx = 0
for i in range(1, N+1):
    if kevin_bacon[i] < min_kevin_bacon:
        min_kevin_bacon = kevin_bacon[i]
        min_idx = i

# 결과 출력
print(min_idx)
