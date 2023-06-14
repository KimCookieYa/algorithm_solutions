n = int(input())

dp = [[1] * 10 for __ in range(n)]
for i in range(1, n):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][:j+1])%10007

print(sum(dp[n-1])%10007)