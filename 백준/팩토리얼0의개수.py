import sys

# 입력받기
n = int(sys.stdin.readline())

# 5의 개수 구하기
count = 0
while n >= 5:
    count += n // 5
    n //= 5

# 출력
print(count)