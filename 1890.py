import sys
input = sys.stdin.readline

n = int(input())
maps = [list(map(int, input().split())) for __ in range(n)]

dp = [[0] * n for __ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if maps[i][j] != 0 and dp[i][j] > 0:
            next_x = j + maps[i][j]
            next_y = i + maps[i][j]
            if next_x < n:
                dp[i][next_x] += dp[i][j]
            if next_y < n:
                dp[next_y][j] += dp[i][j]

print(dp[n-1][n-1])