import sys
input = sys.stdin.readline

w, h = map(int, input().split())
x, y = map(int, input().split())

dp = [[0] * (w+1) for __ in range((h+1))]
dp[1][1] = 1
for i in range(1, y+1):
    for j in range(1, x+1):
        if dp[i][j] == 0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000007

for i in range(y, h+1):
    for j in range(x, w+1):
        if dp[i][j] == 0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000007

print(dp[h][w])