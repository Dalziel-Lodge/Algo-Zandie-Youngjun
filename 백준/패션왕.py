T = int(input())

for _ in range(T):
    # 의상 수 입력
    n = int(input())

    # 딕셔너리 생성
    clothes = {}

    # 의상 종류별로 수 파악
    for _ in range(n):
        name, category = input().split()
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1

    # 경우의 수 계산
    result = 1
    for value in clothes.values():
        result *= (value + 1)

    # 알몸인 경우의 수 제외
    result -= 1

    # 결과 출력
    print(result)