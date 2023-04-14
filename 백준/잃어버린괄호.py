a = input().split('-')
#-를 기준으로 분리한다.
num = []

for i in a:
    cnt = 0
    s = i.split('+') #+가 포함되어 있다면, 분리 없으면 그냥 더하기
    for j in s:
        cnt += int(j) #+를 기준으로 분리하고 +를 계산한다.
    num.append(cnt) #리스트에 추가
n = num[0] #첫번째 요소가 첫번째 값
for i in range(1, len(num)): #두번째 요소 부터 다 빼준다.
    n -= num[i]
print(n)