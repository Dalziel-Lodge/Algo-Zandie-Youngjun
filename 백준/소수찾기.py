import sys

n = int(input())

numbers = list(map(int, input().split()))
count = 0


for i in numbers:
    if i == 2:
        count += 1
        continue
    for j in range(2, i):
        if i % j == 0:
            break
        elif j == i-1:
            count += 1


print(count)