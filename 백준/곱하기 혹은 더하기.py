#각 자리가ㅏ 숫자 (0~9)로만 주어진 문자열 S
#왼쪽에서 오른쪽으로 모든 숫자를 확인
#숫자 사이에 x 혹은 +연산자를 넣기
#가장 큰 수 만들기

#0이면 더하기
#1이면 더하기
#나머지는 무조건 곱하기가 유리함 -> 그리디

s = input() #ex) 12345
result = int(s[0]) #입력받은 문자열 중 첫번째를 int로 변환하여 result에 대입 #문자열 배열로 접근가능함!

for i in range(1, len(s)):
    num = int(s[i])
    if num <= 1 or result <= 1: #곱하려는 수가 1또는 0일때, 기존의 수가 1또는 0일때
        result += num
    else:
        result *= num

print(result)

