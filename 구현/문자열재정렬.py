#알파벳 배문자와 숫자로만 구성된 문자열
#모든 알파벳을 오름차순으로 정렬 후, 모든 숫자를 더한 값을 출력하기

string_input = input()

capitals = []
value = 0

for i in string_input:
    if i.isalpha():
        capitals.append(i)
    else:
        value += int(i) #얘는 배열에 담을 필요가 없네

capitals.sort()

if value != 0:
    capitals.append(str(value))

print(capitals)
print(''.join(capitals)) #''사이에 있는 값을 붙여서 리스트를 연결해준다.