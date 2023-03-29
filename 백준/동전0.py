import sys

n, k = map(int, sys.stdin.readline().split())

coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))

new_coins = [ coin for coin in coins if coin <= k ]
new_coins.reverse()

count = 0

while k != 0:
    for i in new_coins:
        count += k//i
        k = k % i

print(count)

