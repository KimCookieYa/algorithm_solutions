import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for __ in range(n)]
coins.sort()

dp = [1] + [0] * (k)
for i in range(n):
    for j in range(1, k+1):
        if j >= coins[i]:
            dp[j] = dp[j-coins[i]]+dp[j]

print(dp[k])