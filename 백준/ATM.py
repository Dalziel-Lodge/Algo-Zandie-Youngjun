import sys

n = int(sys.stdin.readline().strip())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

sum = 0

#0번째 n번

for i in range(n):
    sum += (n-i)*times[i]

print(sum)