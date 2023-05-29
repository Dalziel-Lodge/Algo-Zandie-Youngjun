from collections import deque
import sys

words = sys.stdin.readline()
cro_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro_words:
    words = words.replace(i, "a")

print(len(words)-1)