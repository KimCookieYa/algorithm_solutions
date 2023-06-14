t = int(input())

dp = [0, 1] + [0] * 9
while t > 0:
    n = int(input())
    def solution(dp, i):
        if i <= 1 or dp[i] > 0:
            return dp[i]
        
        if i < 4:
            dp[i] += 1
        
        if i-1 > 0:
            dp[i] += solution(dp, i-1)
        if i-2 > 0:
            dp[i] += solution(dp, i-2)
        if i-3 > 0:
            dp[i] += solution(dp, i-3)
        return dp[i]
        
    print(solution(dp, n))
    t -= 1