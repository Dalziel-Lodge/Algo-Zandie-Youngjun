n = int(input())
stair = [0] * 301
dp = [0] * 301

for i in range(1, n+1):
    stair[i] = int(input())

#마지막 계단을 밟았을 때니까
#i번째 계단을 밟았을 때를 기준으로 점화식 생각
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
print(stair)

for i in range(3, n+1):
    #이전 계단을 밟았을 때와, 밟지 않았을 때를 나누어 생각
    dp[i] = max(dp[i-2], dp[i-3] + stair[i-1]) + stair[i]
    print(dp)

print(dp[n])




