import sys

n = int(sys.stdin.readline())

numbers = [0]*10001

#data = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(n):
    index = int(sys.stdin.readline())
    numbers[index] += 1

for i in range(len(numbers)):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)
