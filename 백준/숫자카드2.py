import sys

n = int(sys.stdin.readline().strip())
sang = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().split()))

count = {}
for card in sang:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

result = []
for number in numbers:
    if number in count:
        result.append(count[number])
    else:
        result.append(0)

for i in result:
    print(i, end=' ')