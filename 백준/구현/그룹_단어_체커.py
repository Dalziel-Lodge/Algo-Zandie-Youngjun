"""
다른사람의 풀이
a = 0
for i in range(int(input())):
    s = input()
    a += list(s) == sorted(s, key=s.find)
print(a)
"""

import sys

n = int(sys.stdin.readline().strip())
answer = n

for i in range(n):
    word = sys.stdin.readline().strip()
    chars = list()

    for j in range(len(word)):
        if word[j] not in chars:
            chars.append(word[j])
        else:
            if word[j-1] == word[j]:
                continue
            else:
                answer -= 1
                break


print(answer)