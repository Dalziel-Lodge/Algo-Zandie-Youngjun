#n명의 모험가
#x의 공포도
#x공포도의 모험가는 x명과 그룹을 결성해야함
#최대 그룹 수 는?


###생각 최대한 공포도가 작은 애들로 구성하는 게 좋을 것임
#정렬후, 그룹만들기

n = int(input())
data = list(map(int, input().split()))
data.sort() #오름차순 정력

result = 0 #그룹 수
count = 0 #그룹에 포함 된 인원 수

#[1, 2, 2, 2, 3]

for i in data: #오름차순 정렬된 공포도를 순회
 count += 1 #그룹에 인원 추가
 if count >= i: #인원이
     result += 1 #그룹결성
     count = 0

print(result)

result = 0






print(result)