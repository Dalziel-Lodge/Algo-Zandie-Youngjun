import sys

n = int(sys.stdin.readline().strip())

position = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    position.append((x,y))

position.sort(key = lambda x : (x[1], x[0]))

for i in position:
    print(i[0], i[1])

