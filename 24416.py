n = int(input())

answer1 = 0
answer2 = 0

def fib(n):
    global answer1
    if n == 1 or n == 2:
        answer1 += 1
        return 1
    return fib(n-1) + fib(n-2)

def fib2(n):
    global answer2
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        answer2 += 1
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib2(n), answer2)