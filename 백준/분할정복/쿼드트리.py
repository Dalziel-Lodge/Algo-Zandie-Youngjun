import sys

n = int(sys.stdin.readline().strip())
video = []

#10001000

for _ in range(n):
    string = sys.stdin.readline().strip()
    array = []
    for i in string:
        array.append(int(i))
    video.append(array)

#전체가 하나의 수이면, 그 숫자 출력
#다른 수가 발견되면, (4등분)

def find(x, y, size):
    first = video[x][y]
    is_compressed = True

    for i in range(x, x + size):
        for j in range(y , y +size):
            if video[i][j] != first:
                is_compressed = False
                break

    if is_compressed:
        print(first, end = '')

    else:
        size //= 2
        print("(", end = '')
        find(x, y, size)
        find(x, y + size, size)
        find(x + size, y, size)
        find(x + size, y + size, size)
        print(")", end = '')

find(0, 0, n)

