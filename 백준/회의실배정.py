import sys

n = int(sys.stdin.readline().strip())
meetings = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    meetings.append((a,b))

#끝나는 시간이 같은 경우 시작 시간을 기준으로 정렬
meetings.sort(key = lambda x: (x[1], x[0]))

count = 0
end_time = 0


#회의시간들을 돌면서
for meeting in meetings:
    # 시작시간이 끝나는 시간보다 크거나 같다면
    if meeting[0] >= end_time:
        #횟수 추가, 이미 끝나는 시간이 짧은 순서로 정렬이 되어있기때문에 가능
        count += 1
        #end_time을 새로운 값으로 초기화
        end_time = meeting[1]

print(count)