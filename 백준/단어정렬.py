import sys

n = int(sys.stdin.readline().strip())
words = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    words.append(word)

set_words = list(set(words))

sorted_words = []

for i in set_words:
    sorted_words.append((len(i), i))

result = sorted(sorted_words)

for leni, i in result:
    print(i)