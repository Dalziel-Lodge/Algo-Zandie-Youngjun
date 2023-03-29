import sys

t = int(input())
xx = ""
yy = ""

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    if n <= h:
        xx = str(n)
        yy = "01"
        print(xx+yy)
        continue
    elif n % h == 0:
        xx = str(h)
        yy = str(n // h).zfill(2)
        print(xx + yy)
        continue
    xx = str(n % h)
    yy = str(n // h + 1).zfill(2)
    print(xx+yy)

