import sys
from collections import Counter

def find_mode(numbers):
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]

    if len(modes) == 1:
        return modes[0]
    else:
        return sorted(modes)[1]

n = int(sys.stdin.readline().strip())
numbers = []
for _ in range(n):
    numbers.append((int(sys.stdin.readline().strip())))

numbers.sort()

print(round(sum(numbers)/len(numbers)))
print(numbers[len(numbers)//2])
print(find_mode(numbers))
print(max(numbers)-min(numbers))

