import sys
input = sys.stdin.readline

n = int(input())
costs = list(map(int, input().split()))
k = len(costs)

dp = [[0] * n for __ in range(k)]
for i in range(k):
    for j in range(n):
        if j >= i:
            dp[i][j] = max(dp[i][j-i-1]+costs[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[k-1][n-1])