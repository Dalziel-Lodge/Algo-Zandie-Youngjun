#배열에
import sys


def fibonacci(n):
    array = [[-1, -1] for _ in range(n+2)]
    array[0] = [1, 0]
    array[1] = [0, 1]

    for i in range(2, n+1):
        array[i][0] = array[i-1][0] + array[i-2][0]
        array[i][1] = array[i-1][1] + array[i-2][1]

    return array[n]


t = int(sys.stdin.readline().strip())
tests = [int(sys.stdin.readline().strip()) for _ in range(t)]

for test in tests:
    print(*fibonacci(test))





