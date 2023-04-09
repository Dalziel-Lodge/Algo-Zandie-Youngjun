import sys

n, r, c = map(int, sys.stdin.readline().split())\

def visit(size, x, y):
    if size == 1:
        return 0

    size //= 2

    for i in range(4):
        nx = x + size * (i//2)
        ny = y + size * (i % 2)

        if nx <= r < nx + size and ny <= c < ny + size:
            return(i * size * size) + visit(size, nx, ny)

print(visit(2 ** n, 0, 0))