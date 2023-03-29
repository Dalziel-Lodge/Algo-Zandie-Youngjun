import sys

n = int(input())

for _ in range(n):
    array = sys.stdin.readline().strip()
    while '()' in array:
        array = array.replace('()', '')
    if array == '':
        print("YES")
    else:
        print("NO")
