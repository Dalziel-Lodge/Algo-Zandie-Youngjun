import sys

n = int(sys.stdin.readline().strip())

result = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    result.append((int(age), name))

result.sort( key = lambda x: x[0])
for i in result:
    print(i[0], i[1])





