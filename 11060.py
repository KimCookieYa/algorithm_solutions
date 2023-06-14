import sys
input = sys.stdin.readline

n = int(input())
jumps = list(map(int, input().split()))

dp = [-1] * n
dp[0] = 0
for start in range(n-1):
    end = start + jumps[start]
    for i in range(start+1, end+1):
        if i >= n:
            break
        if dp[start] != -1 and dp[i] == -1:
            dp[i] = dp[start]+1
        else:
            dp[i] = min(dp[i], dp[start]+1)

if dp[n-1] == -1:
    print(-1)
else:
    print(dp[n-1])