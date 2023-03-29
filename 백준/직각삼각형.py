import sys

def checkTri(a):
    maxa = max(a) ** 2
    a.remove(max(a))
    sum_rest = 0
    for i in a:
        sum_rest += i**2
    if maxa == sum_rest:
        print("right")
    else:
        print("wrong")

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if a == [0, 0, 0]:
        break
    else:
        checkTri(a)