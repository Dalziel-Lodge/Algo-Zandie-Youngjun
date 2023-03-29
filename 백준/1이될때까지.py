n, k = map(int, input("2개의 숫자를 입력하세요: ").split())

count = 0
#1로빼는 것보다, k로 나누는 것이 가장 빠르게 횟수를 줄일 수 있음.

while n != 1:
    if n % k != 0:
        n -= 1
        count += 1
    else:
        if n < k:
            n -= 1
            count += 1
            continue
        n = n // k
        count += 1



print("답안제출: " + str(count))

