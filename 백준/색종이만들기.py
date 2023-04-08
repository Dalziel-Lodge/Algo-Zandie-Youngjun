import sys

n = int(sys.stdin.readline().strip())
papers = []

for i in range(n):
    papers.append(list(map(int, sys.stdin.readline().split())))


white = 0
blue = 0

def find_square(x, y, size):
    global white, blue
    color = papers[x][y]
    for i in range(x, x + size):
        for j in range(y, y+size):
            if papers[i][j] != color:
                find_square(x, y, size//2)
                find_square(x+size//2, y, size//2)
                find_square(x, y+size//2, size//2)
                find_square(x+size//2, y+size//2, size//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1



find_square(0, 0, n)
print(white)
print(blue)

