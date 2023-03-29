n = int(input())

initializers = []

for i in range(n+1):
    sump = i + sum(map(int, str(i)))
    if sump == n:
        initializers.append(i)


if len(initializers) == 0:
    print('0')
else:
    print(initializers[0])
