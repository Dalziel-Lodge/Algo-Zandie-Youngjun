import sys

n, m = map(int, sys.stdin.readline().split())
hear = set()
look = set()

for _ in range(n):
    hear.add(sys.stdin.readline().strip())

for _ in range(m):
    look.add(sys.stdin.readline().strip())

intersection = sorted(list(hear.intersection(look)))
print(len(intersection))
for i in intersection:
    print(i)