import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

#출력 = 절단기의 최대 높이

#높이를 0부터 증가시키면서, 잘린 나무의 길이 구하기
#나무의 길이가 원하는 나무길이보다 같을 때까지, 커지면 이전 깂
start = 0
end = max(trees)
result = 0

while start <= end:
    total = 0
    mid = (start + end) //2
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)



