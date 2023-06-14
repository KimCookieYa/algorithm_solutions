n = int(input())

dp = [0, 1, 0, 1] + [0] * (n-3)
for i in range(4, n+1):
    if dp[i-1] or dp[i-3]:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[n]:
    print("SK")
else:
    print("CY")