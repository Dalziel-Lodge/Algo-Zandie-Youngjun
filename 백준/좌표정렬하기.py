import sys

n = int(input())

tmp = []
for i in range(n):
    tmp.append(list((map(int, sys.stdin.readline().split()))))

# 키를 여러개 줄 때는 이렇게 한다
tmp.sort(key = lambda x :  (x[0], x[1]))

for i in tmp:
    print(i[0], i[1])
