#첫째 줄에 8x8 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두문자로 구성된 문자
#a1은 1행1열
#나이트가 이동할 수?
#경우의 수는 8가지

#x축이동
#dx = [-2, -2, -1, -1, 1, 1, 2, 2]

#y축이동
#dy = [1, -1, 2, -2, 2, -2, 1, -1]

#문자는 어떻게 처리하지?
input_data = input()
row = int(input_data[1]) #행
column =int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

#각 방향에 대해 이동 가능한지 확인
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0] #현재 행에서 이동
    next_column = column + step[1] #현재 열에서 이동

    #이동 가능한 위치인지 확인
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
