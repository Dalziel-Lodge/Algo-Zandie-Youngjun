import sys

n = int(sys.stdin.readline().strip())

pos = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    pos.append((a-1,b-1))

square = [[False for i in range(100)] for j in range(100)]

for p in pos:
    x, y = p[0], p[1]
    for i in range(x, x+10):
        for j in range(y, y+10):
            square[i][j] = True

count = 0
for i in square:
    for j in i:
        if j:
            count += 1

print(count)


'''
더 간결한 코드

import sys

n = int(sys.stdin.readline().strip())
pos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
square = [[False] * 100 for _ in range(100)]

for x, y in pos:
    for i in range(x - 1, x + 9):
        for j in range(y - 1, y + 9):
            square[i][j] = True

count = sum(sum(row) for row in square)

print(count)

주요 변경사항:
pos 리스트를 리스트 컴프리헨션으로 생성하였습니다.
square 리스트를 [[False] * 100 for _ in range(100)]로 초기화하였습니다.
pos 리스트에서 언패킹을 통해 좌표를 가져오도록 수정하였습니다.
좌표 반복문에서 범위를 (x - 1, x + 9)와 (y - 1, y + 9)로 변경하여 좌표를 더 직관적으로 처리하였습니다.
count를 리스트 컴프리헨션과 sum() 함수를 사용하여 간단하게 계산하였습니다.
'''