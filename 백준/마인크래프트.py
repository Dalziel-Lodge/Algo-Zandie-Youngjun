n, m, b = map(int, input().split())
land = []
for i in range(n):
    land += list(map(int, input().split()))

min_height = min(land)
max_height = max(land)
time = float('inf')
result_height = 0

for height in range(min_height, max_height + 1):
    blocks = b
    cur_time = 0

    for block in land:
        if block > height:
            cur_time += 2 * (block - height)
            blocks += block - height
        else:
            cur_time += height - block
            blocks -= height - block

    if blocks >= 0 and cur_time <= time:
        time = cur_time
        result_height = height

print(time, result_height)

