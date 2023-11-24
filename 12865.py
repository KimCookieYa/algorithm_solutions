import sys

input = sys.stdin.readline

n, k = map(int, input().split())
products = [list(map(int, input().split())) for __ in range(n)]

dp = [[0] * (k + 1) for __ in range(n + 1)]
for i in range(n):
    for j in range(0, k + 1):
        if j >= products[i][0]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - products[i][0]] + products[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(max(dp[n - 1]))
