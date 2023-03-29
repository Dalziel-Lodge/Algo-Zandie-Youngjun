import sys

n = int(sys.stdin.readline().strip())

bigs = []
for i in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    bigs.append((weight, height))

ranks = [1] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if bigs[i][0] < bigs[j][0] and bigs[i][1] < bigs[j][1]:
            ranks[i] += 1

print(*ranks)