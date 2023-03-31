T = int(input())

for _ in range(T):
    N = int(input())
    p = [1, 1, 1, 2, 2]  # 초기값 설정

    if N <= 5:
        print(p[N - 1])
    else:
        for i in range(5, N):
            p.append(p[i - 1] + p[i - 5])
        print(p[-1])