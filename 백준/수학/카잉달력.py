import sys

# 최대 공약수를 구하는 함수
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

t = int(sys.stdin.readline().strip())

for _ in range(t):
    # 입력 받기
    m, n, x, y = map(int, sys.stdin.readline().split())

    # x를 기준으로 y를 맞추기
    while y <= m:
        # x와 y가 같으면 정답
        if x == y:
            print(y)
            break
        # 다음 y값으로 갱신
        y += n

    # 정답을 찾지 못한 경우
    else:
        lcm = m * n // gcd(m, n)  # 최소 공배수 구하기
        while x <= lcm:
            if x % n == y % n:
                print(x)
                break
            x += m
        # 정답을 찾지 못한 경우
        else:
            print(-1)
