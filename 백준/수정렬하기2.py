import sys

n = int(sys.stdin.readline().strip())
tmp = []

for i in range(n):
    tmp.append(int(sys.stdin.readline().strip()))

tmp.sort()

for i in tmp:
    print(i)