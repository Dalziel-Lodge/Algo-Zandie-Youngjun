import sys

n = int(sys.stdin.readline().strip())

houses = []
for _ in range(n):
    string = sys.stdin.readline().strip()
    ns = []
    for s in string:
        ns.append(int(s))
    houses.append(ns)

visited = [[False] * n for _ in range(n)]

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

count_house = {}
house_number = 0

def dfs(x, y):
    visited[x][y] = True
    count_house[house_number] += 1
    for i in d:
        nx = x + i[0]
        ny = y + i[1]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and houses[nx][ny] == 1:
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and houses[i][j] == 1:
            house_number += 1
            count_house[house_number] = 0
            dfs(i, j)

print(house_number)
for i in sorted(count_house.values()):
    print(i)
