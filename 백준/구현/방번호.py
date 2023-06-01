from collections import Counter
import sys

number = list(sys.stdin.readline().strip())
number_counts = Counter(number)
six_nine = (number_counts['6'] + number_counts['9'])

if six_nine % 2 == 0:
    six_nine //= 2
else:
    six_nine = six_nine // 2 + 1

del number_counts['6']
del number_counts['9']

if not number_counts:
    print(six_nine)
elif six_nine > max(number_counts.values()):
    print(six_nine)
else:
    print(max(number_counts.values()))


'''
다른사람의 풀이
import sys
n = sys.stdin.readline().rstrip()

count = [0] * 10 #카운터 대신 사용
for i in n:
    count[int(i)] += 1
count[6] = (count[6] + count[9] + 1) // 2 #애초에 1더해주면 홀수든 짝수든 상관없음
count[9] = 0 #중복 안하기 위해서 0으로 초기화
print(max(count))
'''
