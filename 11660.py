import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for __ in range(n)]
points = [list(map(int, input().split())) for __ in range(m)]

dp = [[0] * (n+1) for __ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]

for point in points:
    sx, sy = point[:2]
    ex, ey = point[2:]
    answer = dp[ex][ey] - dp[sx-1][ey] - dp[ex][sy-1] + dp[sx-1][sy-1]
    print(answer)