

n = int(input())

count = n // 5
n = n % 5

while n % 3 != 0 and count > 0:
    count -= 1
    n += 5

if n % 3 == 0:
    count += n // 3
    print(count)
else:
    print(-1)