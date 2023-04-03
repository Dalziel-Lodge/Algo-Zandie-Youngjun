n = int(input())

#n을 2와 1의 조합으로 나타내는 순열

dp = [0]*1001
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]



print(dp[n] % 10007)