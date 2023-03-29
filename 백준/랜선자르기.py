import sys

lans = []

k, n = map(int, input().split())

for _ in range(k):
    lans.append(int(sys.stdin.readline().strip()))

start = 1
end = max(lans)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for lan in lans:
        count += lan // mid

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)