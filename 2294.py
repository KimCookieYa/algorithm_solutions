import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, k = map(int, input().split())
coins = [int(input()) for __ in range(n)]
coins = list(set(coins))
dp = [0] * (100001)
for coin in coins:
    dp[coin] = 1

def solution(n):
    if dp[n] > 0:
        return dp[n]
    
    min_val = 1e9
    for coin in coins[::-1]:
        if n-coin > 0:
            min_val = min(min_val, solution(n-coin)+1)
    
    dp[n] = min_val
    return dp[n]

answer = solution(k)
if answer == 1e9:
    print(-1)
else:
    print(answer)