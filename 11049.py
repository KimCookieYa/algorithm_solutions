import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
for __ in range(n-1):
    __, c = map(int, input().split())
    nums.append(c)

dp = [[0] * n for __ in range(n)]
for i in range(n):
    for j in range(n-i):
        k = i + j
        
        if j == k:
            continue
        
        dp[j][k] = float('inf')
        for l in range(j, k):
            dp[j][k] = min(dp[j][k], dp[j][l] + dp[l+1][k] + nums[j]*nums[l+1]*nums[k+1])

print(dp[0][-1])