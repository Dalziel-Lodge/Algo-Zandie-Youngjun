n = int(input())

rect = [0]*1001

rect[1] = 1
rect[2] = 3

for i in range(3, n+1):
    rect[i] = (2*rect[i-2] + rect[i-1]) % 10007

print(rect[n])