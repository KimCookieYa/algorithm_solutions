n, k = map(int, input().split())

dp = [[0] * (k+1) for __ in range(n+1)]

def solution(n, k):
    if k == 1:
        dp[n][k] = 1
        return 1
    if dp[n][k] != 0:
        return dp[n][k]
    
    result = 0
    for i in range(0, n+1):
        result = (result + solution(n-i, k-1)) % 1000000000
    dp[n][k] = result
    return result

print(solution(n, k))