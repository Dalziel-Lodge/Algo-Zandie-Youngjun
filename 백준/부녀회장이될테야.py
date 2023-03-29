import sys

t = int(sys.stdin.readline().strip())

def sum(k, n):
    if n == 1:
        return 1
    if k == 0:
        return n
    else:
        sum_tmp = sum(k, n-1) + sum(k-1, n)
        return sum_tmp

for i in range(t):
    k = int(sys.stdin.readline().strip()) #층
    n = int(sys.stdin.readline().strip()) #호
    print(sum(k, n))




#1 4 10 20 35
#1 3 6 10 15
#1 2 3 4 5 ... i