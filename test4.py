import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
smalls = [int(input())-1 for __ in range(m)]

dp = [INF] * n
dp[0] = 0
dp_step = [0] * n
for step in range(n):
    if step in smalls:
        continue
    
    for next_step in [dp_step[step]-1, dp_step[step], dp_step[step]+1]:
        next = step+next_step
        if step < next < n:
            if next not in smalls:
                if dp[next] > dp[step]+1 and (n-1-next >= next_step-1 or next == n-1):
                    dp[next] = dp[step]+1
                    dp_step[next] = next_step

if dp[n-1] == INF:
    print(-1)
else:
    print(dp[n-1])