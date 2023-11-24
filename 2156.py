import sys

input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for __ in range(n)]
dp = [0]

for i in range(1, 3):
    dp.append(dp[i - 1] + wine[i])
    if n == 1:
        break

for i in range(3, n + 1):
    dp.append(max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 1]))

print(dp[-1])
