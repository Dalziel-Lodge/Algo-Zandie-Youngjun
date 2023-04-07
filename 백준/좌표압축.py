import sys

n = int(sys.stdin.readline().strip())
coordinates = list(map(int, sys.stdin.readline().split()))


new_coord = sorted(list(set(coordinates)))
indices = {c: i for i, c in enumerate(new_coord)}

print(indices)

for c in coordinates:
    print(indices[c], end = ' ')

