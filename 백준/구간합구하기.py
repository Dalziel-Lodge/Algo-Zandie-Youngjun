import sys

n, m = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))


pre_sum = [0]*(n+1)

for i in range(1, n+1):
    pre_sum[i] = pre_sum[i-1] + numbers[i-1]

for _ in range(m):
    a, b  = map(int, sys.stdin.readline().split())
    print(pre_sum[b] - pre_sum[a-1])
