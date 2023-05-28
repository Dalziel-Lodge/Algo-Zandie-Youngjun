n, m, k = map(int,input('3개의 숫자를 입력해주세요 : ').split())
# 사용자 입력을 공백기준 split하고 int로 변환하여 n,m,k에 저장
num_list = list(map(int, input().split()))

count = 0
result = 0

print(n, m, k)
print(num_list)

num_list.sort()
print(num_list)

#연속해서 더하지만 않으면 되니까 맨 뒤에놈이랑 그 앞에놈만 사용하게 됨
firstHighValue = num_list[n-1]
secondHighValue = num_list[n-2]

for i in range(m):
    if count < k:
        result += firstHighValue
        count += 1
    elif count == k:
        result += secondHighValue
        count = 0

print(result)
