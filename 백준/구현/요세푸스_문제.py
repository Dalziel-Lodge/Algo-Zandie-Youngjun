import sys

n, k = map(int, sys.stdin.readline().split())

array = [i for i in range(1, n+1)]
answer = []
pos = k - 1

while array:
    length = len(array)
    if pos <= length-1:
        answer.append(array.pop(pos))
        pos += k - 1
    else:
        while pos > length-1:
            pos = pos - length
        answer.append(array.pop(pos))
        pos += k - 1

print("<", end = "")

for item in answer:
    if item == answer[-1]:
        print(item, end = "")
    else:
        print(item, end = ", ")


print(">", end = "")
