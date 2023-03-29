import sys

n = int(sys.stdin.readline().strip())
movie = 666

while True:
    if n == 0:
        break
    if '666' in str(movie):
        n -= 1
    movie += 1

print(movie -1)

# 666 1666 2666 3666 4666 5666 6066
# _666_
