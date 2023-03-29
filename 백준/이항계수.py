import sys
n, k = map(int, sys.stdin.readline().split())

son = 1
mom = 1

if k == 0:
        print(1)
        exit()
else:
    for i in range(k):
        son *= (n-i)
        mom *= (i+1)

print(son // mom)



