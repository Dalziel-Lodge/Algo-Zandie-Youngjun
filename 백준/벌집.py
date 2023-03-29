#육각형
#1, 7, 19, 37
#0 1 3 6 10

n = int(input())
cnt = 1

beehouse = 1
while n > beehouse:
    beehouse += (6 * cnt)
    cnt += 1

print(cnt)