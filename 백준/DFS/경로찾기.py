import sys

# 정점의 개수 입력받기
n = int(sys.stdin.readline().strip())

# 인접행렬 입력받기
adj_matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# DFS 함수 구현
def dfs(v):
    # 현재 노드 방문 체크
    visited[v] = True
    # 인접한 노드들 중에서 방문하지 않은 노드를 재귀호출로 방문
    for i in range(n):
        if adj_matrix[v][i] == 1 and not visited[i]:
            dfs(i)

# 모든 노드에 대해서 DFS 실행하며 방문 체크
for i in range(n):
    visited = [False for _ in range(n)]
    dfs(i)
    # 방문한 노드들 출력
    for j in range(n):
        print(int(visited[j]), end=" ")
    print()